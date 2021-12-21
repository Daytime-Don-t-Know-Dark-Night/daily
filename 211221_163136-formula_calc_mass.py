# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  calc_result.py
# 日期时间：2021/12/21，15:21

# 计算方式-参考网站: https://massbank.eu/MassBank/js/MassCalc.js
import re

atomic_mass = {
    "H": 1.0078250321,
    "He": 4.0026032497,
    "Li": 7.0160040,
    "Be": 9.0121821,
    "B": 11.0093055,
    "C": 12.0,
    "N": 14.0030740052,
    "O": 15.9949146221,
    "F": 18.99840320,
    "Ne": 19.9924401759,
    "Na": 22.98976967,
    "Mg": 23.98504190,
    "Al": 26.98153844,
    "Si": 27.9769265327,
    "P": 30.97376151,
    "S": 31.97207069,
    "Cl": 34.96885271,
    "Ar": 35.96754628,
    "K": 38.9637069,
    "Ca": 39.9625912,
    "Sc": 44.9559102,
    "Ti": 47.9479471,
    "V": 50.9439637,
    "Cr": 51.9405119,
    "Mn": 54.9380496,
    "Fe": 55.9349421,
    "Co": 58.9332002,
    "Ni": 57.9353479,
    "Cu": 62.9296011,
    "Zn": 63.9291466,
    "Ga": 68.925581,
    "Ge": 73.9211782,
    "As": 74.9215964,
    "Se": 79.9165218,
    "Br": 78.9183376,
    "Kr": 83.911507,
    "Rb": 84.9117893,
    "Sr": 87.9056143,
    "Y": 88.9058479,
    "Zr": 95.908276,
    "Nb": 92.9063775,
    "Mo": 91.906810,
    "Tc": 96.906365,
    "Ru": 101.9043495,
    "Rh": 102.905504,
    "Pd": 105.903483,
    "Ag": 106.905093,
    "Cd": 113.9033581,
    "In": 114.903878,
    "Sn": 119.9021966,
    "Sb": 120.9038180,
    "Te": 129.9062228,
    "I": 126.904468,
    "Xe": 131.9041545,
    "Cs": 132.905447,
    "Ba": 137.905241,
    "La": 138.906348,
    "Ce": 139.905434,
    "Pr": 140.907648,
    "Nd": 141.907719,
    "Pm": 144.912744,
    "Sm": 151.919728,
    "Eu": 152.921226,
    "Gd": 157.924101,
    "Tb": 158.925343,
    "Dy": 163.929171,
    "Ho": 164.930319,
    "Er": 165.930290,
    "Tm": 168.934211,
    "Yb": 173.9388581,
    "Lu": 174.9407679,
    "Hf": 179.9465488,
    "Ta": 180.947996,
    "W": 183.9509326,
    "Re": 186.9557508,
    "Os": 191.961479,
    "Ir": 192.962924,
    "Pt": 194.964774,
    "Au": 196.966552,
    "Hg": 201.970626,
    "Tl": 204.974412,
    "Pn": 207.976636,
    "Bi": 208.980383,
    "Po": 209.982857,
    "At": 209.987131,
    "Rn": 222.0175705,
    "Fr": 223.0197307,
    "Ra": 226.0254026,
    "Ac": 227.0277470,
    "Th": 232.0380504,
    "Pa": 231.0358789,
    "U": 238.0507826,
    "Np": 237.0481673,
    "Pu": 239.0521565,
    "Am": 243.0613727,
    "Cm": 247.070347,
    "Bk": 247.070299,
    "Cf": 251.079580,
    "Es": 252.082970,
    "Fm": 257.095099
}


# 获得原子组合列表
def get_atomic_list(formula):
    atomic_list = []
    next_char = ""
    sub_str_index = 0
    end_chr_flag = 0

    # 在适当的位置分隔（原子符号+原子数）['C10', 'H9', 'Cl', 'N4', 'O2', 'S']
    n = len(formula)
    for i in range(n):
        if (i + 1) < n:
            next_char = formula[i + 1]
        else:
            end_chr_flag = 1
        # 如果没有下一个字符，或者如果下一个字符是大写字母，则分隔
        if (end_chr_flag == 1) or (next_char.isupper()):
            atomic_list.append(formula[sub_str_index:(i + 1)])
            sub_str_index = i + 1

    return atomic_list


# 计算mass分子量
def mass_calc(atomic_list):
    mass = 0.0
    n = len(atomic_list)
    for i in range(n):
        atom_num = 0
        sub_str_index = 0
        atom_num_flag = 0
        str_item = atomic_list[i]

        # 把原子分成原子符号和原子数
        for j in range(len(str_item)):
            if re.search(r'\d', str_item):  # 如果有数字
                sub_str_index = str_item.index(re.findall(r'\d+', str_item)[0])  # atomic_list[i] 中第一个数字的子串的位置
                atom_num_flag = 1
                break

        # 没有原子数的情况
        if not atom_num_flag:
            atom_num = 1
            sub_str_index = len(str_item)

        # 在原子数之前或字符串结束前为原子符号
        atom = str_item[0:sub_str_index]

        # 原子符号的原子数
        if atom_num_flag:
            atom_num = str_item[sub_str_index:]

        # 把每个原子的mass全部加在一起
        mass += atomic_mass[atom] * float(atom_num)
    return mass


atomic_list_result = get_atomic_list('C10H9ClN4O2S')
print(atomic_list_result)
mass_result = mass_calc(atomic_list_result)
print(mass_result)
