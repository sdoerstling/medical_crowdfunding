#import libraries
import asyncio
import aiohttp
from itertools import islice
import json
import re
import datetime
import time
from random import sample
import pandas as pd
import async_timeout
import sys

#define proxy address
PROXY = ""

#define input index
input_index = int(sys.argv[1])

#define helper functions
def findkeys(node, kv):
    if isinstance(node, list):
        for i in node:
            for x in findkeys(i, kv):
                yield x
    elif isinstance(node, dict):
        if kv in node:
            yield node[kv]
        for j in node.values():
            for x in findkeys(j, kv):
                yield x

#get updates
async def getUpdates(cur_camp, session):
    print("Starting updates for %s" % cur_camp)
    update_base_begin = "https://gateway.gofundme.com/web-gateway/v1/feed/"
    update_base_end = "/updates?limit=3&offset="
    update_list = []
    update_resp_status = []
    update_data = {
        "update_list" : update_list,
        "update_resp_status" : update_resp_status,
        "update_data_error" : 0
    }
    offset = 0
    while True:
        #duplicates -> in case website is buggy, assume that no more than 50 updates
        if(offset > 50):
            return update_data

        url = update_base_begin + cur_camp + update_base_end + str(offset)
        async with session.get(url, proxy = PROXY) as resp:
            resp_status = resp.status
            update_data['update_resp_status'] = resp_status

            if resp_status != 200:
                break
            else:
                try:
                    update_content = await resp.text()
                    update_json = json.loads(update_content)
                    update_list += update_json['references']['updates']

                    #increase offset
                    if(update_json['meta']['has_next']):
                        offset += 3
                    else:
                        break
                except:
                    update_data['update_data_error'] = 1
                    break
    print("Response updates for %s" % cur_camp)
    return update_data

#get comments
async def getComments(cur_camp, session):
    print("Starting comments for %s" % cur_camp)
    comment_base_begin = "https://gateway.gofundme.com/web-gateway/v1/feed/"
    comment_base_end = "/comments?limit=20&offset="
    comment_list = []
    comment_ids = []
    comment_resp_status = []
    comment_data = {
        "comment_list" : comment_list,
        "comment_ids" : comment_ids,
        "comment_resp_status" : comment_resp_status,
        "comment_data_error" : 0
    }
    offset = 0
    while True:
        url = comment_base_begin + cur_camp + comment_base_end + str(offset)
        async with session.get(url, proxy = PROXY) as resp:
            resp_status = resp.status
            comment_data["comment_resp_status"].append(resp.status)

            if resp_status != 200:
                break
            else:
                try:
                    comment_content = await resp.text()
                    comment_json = json.loads(comment_content)

                    #add to list of comment ids
                    curr_comment_ids = list(findkeys(comment_json, "comment_id"))

                    #add this b/c website has bugs, has infinite loops
                    #if duplicates -> only get unique and return
                    if curr_comment_ids[0] in comment_ids:
                        for item in comment_json['references']['contents']:
                            #unique
                            if item['comment']['comment_id'] not in comment_ids:
                                comment_list.append(item.copy())
                            else:
                                return comment_data

                    comment_ids += curr_comment_ids
                    comment_list += comment_json['references']['contents']

                    #increase offset
                    if(comment_json['meta']['has_next']):
                        offset += 20
                    else:
                        break
                except:
                    comment_data['comment_data_error'] = 1
                    break

    print("Response comments for %s" % cur_camp)
    return comment_data

#get donations
async def getDonors(cur_camp, session):
    print("Starting donors for %s" % cur_camp)
    donor_base_begin = "https://gateway.gofundme.com/web-gateway/v1/feed/"
    donor_base_end = "/donations?limit=100&offset="
    donor_list = []
    donor_resp_status = []
    donor_data = {
        "donor_list" : donor_list,
        "donor_resp_status" : donor_resp_status,
        "donor_reached_max" : 0,
        "donor_data_error" : 0
    }
    offset = 0
    while True:
        # offset greater than 1000
        if offset >= 1000:
            donor_data['donor_reached_max'] = 1
            break

        url = donor_base_begin + cur_camp + donor_base_end + str(offset) + "&sort=recent"

        async with session.get(url, proxy = PROXY) as resp:

            resp_status =  resp.status

            donor_data['donor_resp_status'].append(resp.status)

            if resp_status != 200:
                break
            else:
                try:
                    donor_content = await resp.text()
                    donor_json = json.loads(donor_content)
                    donor_list += donor_json['references']['donations']

                    #increase offset
                    if(donor_json['meta']['has_next']):
                        offset += 100
                    else:
                        break
                except:
                    donor_data['donor_data_error'] = 1
                    break

    print("Response donors for %s" % cur_camp)
    return donor_data




async def getURL(url):
    print("Starting %s" % url)
    await asyncio.sleep(1)
    camp_data = {
        "scrape" : {
            "url" : url,
            "resp_status" : None,
            "date_scrape" : None,
            "cat" : None,
            "target_cat" : None,
            "activity_status" : None,
            "country" : None
        },
        "feed" : None,
        "donor" : None,
        "comment" : None,
        "update" : None
    }

    connector=aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector = connector) as session:
        async with session.get(url, proxy = PROXY) as resp:

            print("Response %s" % url)
            resp_status =  resp.status
            resp_headers =  resp.headers
            try:
                date_scrape = resp_headers['Date']
            except:
                date_scrape = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + 'EST'

            if resp_status != 200:
                camp_data['scrape']['resp_status'] = resp_status
                camp_data['scrape']['date_scrape'] = date_scrape
                return camp_data
            else:
                camp_data['scrape']['resp_status'] = resp_status
                camp_data['scrape']['date_scrape'] = date_scrape

            content = await resp.text()
            camp_json = json.loads(re.findall(r'window\.initialState = ({.*?});', content)[0])
            feed = camp_json['feed']
            camp_data['scrape']['cat'] = feed['campaign']['category_id']
            camp_data['scrape']['activity_status'] = feed['campaign']['state']
            camp_data['scrape']['country'] = feed['campaign']['location']['country']


            if feed['campaign']['category_id'] not in [11]:
                camp_data['scrape']['target_cat'] = 0
                return camp_data
            if feed['campaign']['state'] != "active":
                camp_data['scrape']['target_cat'] = 1
                return camp_data
            if feed['campaign']['location']['country'] != "US":
                camp_data['scrape']['target_cat'] = 1
                return camp_data
            else:
                camp_data['scrape']['target_cat'] = 1
                camp_data['feed'] = feed


            cur_camp = feed['campaign']['url']

            #donations
            camp_data['donor'] = await getDonors(cur_camp, session)
            #don_task = loop.create_task(getDonors(cur_camp, session))
            #camp_data['donor'] = await don_task


            #comments
            camp_data['comment'] = await getComments(cur_camp, session)
            #com_task = loop.create_task(getComments(cur_camp, session))
            #camp_data['comment'] = await com_task

            #updates
            camp_data['update'] = await getUpdates(cur_camp, session)
            #up_task = loop.create_task(getUpdates(cur_camp, session))
            #camp_data['update'] = await up_task


    return camp_data


#function to limit number of simultaneous tasks
def limited_as_completed(coros, limit):
    """
    Run the coroutines (or futures) supplied in the
    iterable coros, ensuring that there are at most
    limit coroutines running at any time.

    Return an iterator whose values, when waited for,
    are Future instances containing the results of
    the coroutines.
    Results may be provided in any order, as they
    become available.

    Courtesy of: https://github.com/andybalaam/asyncioplus
    """
    futures = [
        asyncio.ensure_future(c)
        for c in islice(coros, 0, limit)
    ]
    async def first_to_finish():
        while True:
            await asyncio.sleep(0)
            for f in futures:
                if f.done():
                    futures.remove(f)
                    try:
                        newf = next(coros)
                        futures.append(
                            asyncio.ensure_future(newf))
                    except StopIteration as e:
                        pass
                    return f.result()
    while len(futures) > 0:
        yield first_to_finish()


#function to await tasks and add to output data when complete
async def save_when_done(tasks, data):
    for res in limited_as_completed(tasks, 100):
    #for res in tasks:
        r = await res
        data.append(r)


        feed = pd.DataFrame(i['feed']['campaign'] for i in data if i['feed'] is not None)
        if len(feed) >= 100000:
            print("--- Hit sample size ---")
            raise Exception


#load data
print("Loading campaigns")
data_filename = "data/sitemaps_combined_" + str(input_index) + ".csv"
campaigns = pd.read_csv(data_filename)
urls = campaigns.iloc[:,1].to_list()

#split data into bits of 1000
#n = 1000  #chunk row size
#url_list = [urls[i:i + n] for i in range(0, len(urls), n)]


#define empty list to store data
data = []

#create generator of coroutines
#coros = (getURL(url) for url in urls)
coros = (getURL(url) for url in urls)

#create and run event loop
print("Starting loop")
start_time = time.time()
loop = asyncio.get_event_loop()
try:
    #loop.run_until_complete(save_when_done(coros, data))
    task = loop.create_task(save_when_done(coros, data))
    loop.run_until_complete(task)
    loop.stop()
    loop.close()
except Exception:
    pending = asyncio.Task.all_tasks()
    [task.cancel() for task in pending]
    #tasks.cancel()
    loop.stop()
finally:
    loop.close()


#save data
filename = 'data_' + str(input_index) + '.json'
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print("done")
time_end = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print("--- %s seconds ---" % (time.time() - start_time))



