# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import datetime


class LApikey(models.Model):
    api_key = models.CharField(db_column='API_KEY', primary_key=True, max_length=50)  # Field name made lowercase.
    reg_date = models.DateTimeField(db_column='REG_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'l_apikey'


class LChampion(models.Model):
    champion_id = models.CharField(db_column='CHAMPION_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    champion_eng_name = models.CharField(db_column='CHAMPION_ENG_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    champion_kor_name = models.CharField(db_column='CHAMPION_KOR_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reg_date = models.DateTimeField(db_column='REG_DATE', blank=True, null=True)  # Field name made lowercase.
    upd_date = models.DateTimeField(db_column='UPD_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'l_champion'


class LUser(models.Model):
    user_game_id = models.CharField(db_column='USER_GAME_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    user_type = models.CharField(db_column='USER_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    game_lvl = models.IntegerField(db_column='GAME_LVL', blank=True, null=True)  # Field name made lowercase.
    euc_id = models.CharField(db_column='EUC_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    account_id = models.CharField(db_column='ACCOUNT_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puuid = models.CharField(db_column='PUUID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reg_date = models.DateTimeField(db_column='REG_DATE', blank=True, null=True)  # Field name made lowercase.
    upd_date = models.DateTimeField(db_column='UPD_DATE', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'l_user'



class LUserMatch(models.Model):
    user_game_id = models.CharField(db_column='USER_GAME_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    game_match_id = models.CharField(db_column='GAME_MATCH_ID', max_length=50)  # Field name made lowercase.
    #champion_id = models.IntegerField(db_column='CHAMPION_ID', blank=True, null=True)  # Field name made lowercase.
    champion_id = models.ForeignKey(LChampion, db_column='CHAMPION_ID', on_delete=models.CASCADE)  # Field name made lowercase.    
    que_type = models.IntegerField(db_column='QUE_TYPE', blank=True, null=True)  # Field name made lowercase.
    season = models.IntegerField(db_column='SEASON', blank=True, null=True)  # Field name made lowercase.
    game_date = models.DateTimeField(db_column='GAME_DATE', blank=True, null=True)  # Field name made lowercase.
    game_role = models.CharField(db_column='GAME_ROLE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lane = models.CharField(db_column='LANE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_date = models.DateTimeField(db_column='REG_DATE', blank=True, null=True)  # Field name made lowercase.
    upd_date = models.DateTimeField(db_column='UPD_DATE', blank=True, null=True)  # Field name made lowercase.
    kills = models.IntegerField(db_column='KILLS', blank=True, null=True)  # Field name made lowercase.
    deaths = models.IntegerField(db_column='DEATHS', blank=True, null=True)  # Field name made lowercase.
    assists = models.IntegerField(db_column='ASSISTS', blank=True, null=True)  # Field name made lowercase.
    win_flag = models.CharField(db_column='WIN_FLAG', max_length=10, blank=True, null=True)  # Field name made lowercase.

    @property
    def position_img(self):
        
        if self.game_role == "DUO_SUPPORT":
            game_role_conv = "support"
        else:
            game_role_conv = self.game_role

        if self.lane == "BOTTOM":
            lane_conv = "ad"
        elif self.lane == "TOP":
            lane_conv = "top"
        elif self.lane == "JUNGLE":
            lane_conv = "jg"
        elif self.lane == "MID":
            lane_conv = "mid"
        else:
            lane_conv = ""

        if game_role_conv == "support":
            position_img_conv = game_role_conv
        else:
            position_img_conv = lane_conv
        return position_img_conv

    class Meta:
        managed = False
        db_table = 'l_user_match'
        unique_together = (('user_game_id', 'game_match_id'),)


class LUserRank(models.Model):
    user_game_id = models.CharField(db_column='USER_GAME_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    que_type = models.CharField(db_column='QUE_TYPE', max_length=50)  # Field name made lowercase.
    tier = models.CharField(db_column='TIER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rank_lvl = models.CharField(db_column='RANK_LVL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    league_pt = models.IntegerField(db_column='LEAGUE_PT', blank=True, null=True)  # Field name made lowercase.
    wins_cnt = models.IntegerField(db_column='WINS_CNT', blank=True, null=True)  # Field name made lowercase.
    losses_cnt = models.IntegerField(db_column='LOSSES_CNT', blank=True, null=True)  # Field name made lowercase.
    reg_date = models.DateTimeField(db_column='REG_DATE', blank=True, null=True)  # Field name made lowercase.
    upd_date = models.DateTimeField(db_column='UPD_DATE', blank=True, null=True)  # Field name made lowercase.

    @property
    def tier_img(self):
        return self.tier.lower()

    @property
    def diff_min(self):
        upd_date_conv = self.upd_date.strftime('%Y-%m-%d %H:%M:%S')
        curr_now = datetime.datetime.now()
        now_conv = curr_now.strftime('%Y-%m-%d %H:%M:%S')
        diff_day_conv = datetime.datetime.strptime(now_conv, "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(upd_date_conv, "%Y-%m-%d %H:%M:%S")        
        return int(diff_day_conv.seconds / 60)

    @property
    def diff_hour(self):
        upd_date_conv = self.upd_date.strftime('%Y-%m-%d %H:%M:%S')
        curr_now = datetime.datetime.now()
        now_conv = curr_now.strftime('%Y-%m-%d %H:%M:%S')
        diff_day_conv = datetime.datetime.strptime(now_conv, "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(upd_date_conv, "%Y-%m-%d %H:%M:%S")
        return int(diff_day_conv.seconds / 60 / 60)

    @property
    def diff_day(self):
        upd_date_conv = self.upd_date.strftime('%Y-%m-%d %H:%M:%S')
        curr_now = datetime.datetime.now()
        now_conv = curr_now.strftime('%Y-%m-%d %H:%M:%S')
        diff_day_conv = datetime.datetime.strptime(now_conv, "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(upd_date_conv, "%Y-%m-%d %H:%M:%S")
        return int(diff_day_conv.days)

    class Meta:
        managed = False
        db_table = 'l_user_rank'
        unique_together = (('user_game_id', 'que_type'),)
