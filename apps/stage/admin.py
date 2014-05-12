# -*- coding: utf-8 -*-

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.stage.models import Battle, Stage, EliteStage, ChallengeStage, ActivelyStage
from apps.hero.models import Monster
from libs.hero import monster_power

class BattleResources(resources.ModelResource):
    class Meta:
        model = Battle

class StageResources(resources.ModelResource):
    class Meta:
        model = Stage

class EliteStageResources(resources.ModelResource):
    class Meta:
        model = EliteStage

class ChallengeStageResources(resources.ModelResource):
    class Meta:
        model = ChallengeStage


class ActivelyStageResources(resources.ModelResource):
    class Meta:
        model = ActivelyStage


class BattleAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'level_limit', 'des',)
    resource_class = BattleResources

class StageAdmin(ImportExportModelAdmin):
    list_display = (
        'id', 'name', 'bg', 'level', 'strength_modulus', 'tp', 'battle',
        'open_condition', 'Monsters', 'Powers',
        'normal_exp', 'normal_gold', 'normal_drop',
        'first_exp', 'first_gold', 'first_drop',
        'star_exp', 'star_gold', 'star_drop',
    )

    list_filter = ('battle',)
    resource_class = StageResources

    def Monsters(self, obj):
        monsters = obj.monsters.split(',')
        text = []
        for i in range(0, 9, 3):
            text.append(','.join(monsters[i: i+3]))

        return "<br />".join(text)
    Monsters.allow_tags = True
    Monsters.short_description = "怪物ID"


    def Powers(self, obj):
        ms = [int(i) for i in obj.monsters.split(',')]
        text = []
        p = 0
        for line in zip(ms[::3], ms[1::3], ms[2::3]):
            line_text = []
            line_p = 0
            for m in line:
                if m == 0:
                    line_text.append('0')
                else:
                    mobj = Monster.objects.get(id=m)
                    mp = monster_power(obj.strength_modulus, mobj, obj.level)
                    line_p += mp
                    p += mp
                    line_text.append(str(mp))

            line_text.append(" | {0}".format(line_p))
            text.append(', '.join(line_text))

        text.append('-' * 6)
        text.append(str(p))
        return "<br />".join(text)
    Powers.allow_tags = True



class EliteStageAdmin(ImportExportModelAdmin):
    list_display = (
        'id', 'name', 'battle', 'bg', 'level', 'strength_modulus', 'times',
        'open_condition', 'Monsters', 'Powers',
        'normal_exp', 'normal_gold', 'normal_drop',
    )

    resource_class = EliteStageResources

    def Monsters(self, obj):
        monsters = obj.monsters.split(',')
        text = []
        for i in range(0, 9, 3):
            text.append(','.join(monsters[i: i+3]))

        return "<br />".join(text)
    Monsters.allow_tags = True
    Monsters.short_description = "怪物ID"


    def Powers(self, obj):
        ms = [int(i) for i in obj.monsters.split(',')]
        text = []
        p = 0
        for line in zip(ms[::3], ms[1::3], ms[2::3]):
            line_text = []
            line_p = 0
            for m in line:
                if m == 0:
                    line_text.append('0')
                else:
                    mobj = Monster.objects.get(id=m)
                    mp = monster_power(obj.strength_modulus, mobj, obj.level)
                    line_p += mp
                    p += mp
                    line_text.append(str(mp))

            line_text.append(" | {0}".format(line_p))
            text.append(', '.join(line_text))

        text.append('-' * 6)
        text.append(str(p))
        return "<br />".join(text)
    Powers.allow_tags = True




class ChallengeStageAdmin(ImportExportModelAdmin):
    list_display = (
        'id', 'name', 'level', 'char_level_needs', 'open_condition_id', 'open_condition_amount',
        'power_range',
        'aid_limit', 'time_limit', 'reward_gold'
    )

    resource_class = ChallengeStageResources



class ActivelyStageAdmin(ImportExportModelAdmin):
    list_display = (
        'id', 'name', 'battle_name', 'tp', 'bg', 'level', 'strength_modulus', 'char_level',
        'Monsters', 'Powers',
        'normal_exp', 'normal_gold', 'normal_drop',
    )

    resource_class = ActivelyStageResources

    def Monsters(self, obj):
        monsters = obj.monsters.split(',')
        text = []
        for i in range(0, 9, 3):
            text.append(','.join(monsters[i: i+3]))

        return "<br />".join(text)
    Monsters.allow_tags = True
    Monsters.short_description = "怪物ID"


    def Powers(self, obj):
        ms = [int(i) for i in obj.monsters.split(',')]
        text = []
        p = 0
        for line in zip(ms[::3], ms[1::3], ms[2::3]):
            line_text = []
            line_p = 0
            for m in line:
                if m == 0:
                    line_text.append('0')
                else:
                    mobj = Monster.objects.get(id=m)
                    mp = monster_power(obj.strength_modulus, mobj, obj.level)
                    line_p += mp
                    p += mp
                    line_text.append(str(mp))

            line_text.append(" | {0}".format(line_p))
            text.append(', '.join(line_text))

        text.append('-' * 6)
        text.append(str(p))
        return "<br />".join(text)
    Powers.allow_tags = True


admin.site.register(Battle, BattleAdmin)
admin.site.register(Stage, StageAdmin)
admin.site.register(EliteStage, EliteStageAdmin)
admin.site.register(ChallengeStage, ChallengeStageAdmin)
admin.site.register(ActivelyStage, ActivelyStageAdmin)
