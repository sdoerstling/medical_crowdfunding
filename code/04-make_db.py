import sqlite3

conn = sqlite3.connect("gfm.db")

c = conn.cursor()

#create scrape_tb
c.execute(
''' CREATE TABLE scrape_tb (
	camp_id integer primary key,
	url text,
	resp_status int,
	date_scrape text,
	cat int,
	target_cat int,
	activity_status int,
	country int
)''')
conn.commit()

#create feed_tb
c.execute(
''' CREATE TABLE feed_tb (
	feed_id integer primary key,
	id int,
	campaign_id int,
	auto_fb_post_mode text,
	has_beneficiary text,
	category_id int,
	charity_id int,
	is_charity text,
	currencycode text,
	current_amount real,
	default_url text,
	donation_count int,
	comments_enabled text,
	donations_enabled text,
	has_donations text,
	has_gfm_org_donation text,
	fund_description text,
	fund_description_excerpt text,
	fund_name text,
	goal_amount real,
	media_type int,
	project_type int,
	template_id int,
	turn_off_donations int,
	url text,
	user_id int,
	user_first_name text,
	user_last_name text,
	user_facebook_id real,
	user_profile_url text,
	media_id text,
	visible_in_search text,
	status int,
	deactivated text,
	in_degraded_mode text,
	state text,
	is_launched text,
	campaign_image_url text,
	created_at text,
	launch_date text,
	social_share_last_update text,
	is_business text,
	is_team text,
	is_partner text,
	city text,
	country text,
	postal_code int,
	bene_id int,
	bene_user_id int,
	bene_person_id int,
	bene_first_name text,
	bene_last_name text,
	bene_is_placeholder text,
	bene_profile_url text,
	campaign_photo_url text,
	team_name text,
	team_pic_url text,
	team_media_type int,
	team_pub_attr text,
	team_invite_limit int,
	team_status int,
	team_created_date text,
	team_updated_date text,
	donor_resp_status text,
	donor_reached_max int,
	donor_data_error int
)''')
conn.commit()

#create donation_tb
c.execute(
''' CREATE TABLE donation_tb (
	don_id integer primary key,
	online_id integer,
	url text,
	don_amt real,
	don_offline text,
	don_anon int,
	don_name text,
	don_date text,
	don_profile text,
	don_verified text
)''')
conn.commit()

#create team_member_tb
c.execute(
''' CREATE TABLE team_member_tb (
	team_member_id integer primary key,
	url text,
	team_mem_amt real,
	team_mem_fb text,
	team_mem_first_name text,
	team_mem_id int,
	team_mem_last_name text,
	team_mem_gfm_profile text,
	team_mem_don_attr int,
	team_mem_profile text,
	team_mem_role text,
	team_mem_status int,
	team_mem_person_id int,
	team_mem_locale text
)''')
conn.commit()

#create comment_tb
c.execute(
''' CREATE TABLE comment_tb (
	comment_id integer primary key,
	ugc_id int,
	ugc_root_id int,
	name text,
	status real,
	time_stamp text,
	profile_url text,
	url text,
	donation_amount real,
	amount real,
	is_offline text,
	is_anonymous text,
	created_at text,
	comment_id_gfm real,
	comment_text text,
	deny_delete text,
	comment_data_error int
)''')
conn.commit()

#create update_tb
c.execute(
''' CREATE TABLE update_tb (
	update_id integer primary key,
	id int,
	author text,
	author_type text,
	user_profile_url text,
	media_type int,
	status int,
	update_text text,
	created_at text,
	url text,
	photo_url text,
	update_data_error int
)''')
conn.commit()


conn.close()
