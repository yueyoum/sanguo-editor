# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/24/14'

def cal_power(attack, defense, hp, crit):
    a = attack * 2.5 * (1 + crit / 200.0)
    b = hp + defense * 5
    return int(a + b)


STEP_DIFF = 1.08
def hero_calculate(modules, level, step, quality, growing):
    step_adjust = pow(STEP_DIFF, step)
    value = modules * (step+1) * (4-quality) * 1.2 + level * growing * step_adjust
    return value


def hero_attack(level, step, quality, growing):
    return hero_calculate(20, level, step, quality, growing)


def hero_defense(level, step, quality, growing):
    return hero_calculate(15, level, step, quality, growing)


def hero_hp(level, step, quality, growing):
    return hero_calculate(45, level, step, quality, growing)


def cal_monster_property(monster, level):
    attack = hero_attack(level, 0, monster.quality, monster.attack)
    defense = hero_defense(level, 0, monster.quality, monster.defense)
    hp = hero_hp(level, 0, monster.quality, monster.hp)

    return int(attack), int(defense), int(hp)

def monster_power(strength_modulus, monster, level):
    a, d, h = cal_monster_property(monster, level)
    a *= strength_modulus
    d *= strength_modulus
    h *= strength_modulus
    return cal_power(a, d, h, monster.crit)

