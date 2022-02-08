from django.db import models

class Game(models.Model):
    id = models.AutoField(db_column='ID_GAME', primary_key=True)
    event_game = models.CharField(db_column='EVENT_GAME', max_length=255)
    site_game = models.CharField(db_column='SITE_GAME', max_length=255)
    date_game = models.CharField(db_column='DATE_GAME', max_length=255)
    round_game = models.CharField(db_column='ROUND_GAME', max_length=255, null=False)
    white_player = models.CharField(db_column='WHITE_PLAYER', max_length=255, null=False)
    black_palyer = models.CharField(db_column='BLACK_PLAYER', max_length=255, null=False)
    result = models.CharField(db_column='RESULT', max_length=255)
    white_elo = models.CharField(db_column='WHITE_ELO', max_length=255)
    black_elo = models.CharField(db_column='BLACK_ELO', max_length=255)
    eco = models.CharField(db_column='ECO', max_length=255)
    date_modif = models.DateTimeField(db_column='DATE_MODIF')
    game_cmd = models.CharField(db_column='GAME_CMD', max_length=255)

    class Meta:
        managed = False
        db_table = 'TBI_GAME'