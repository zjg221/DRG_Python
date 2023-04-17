from drg_group.suzhou_2023.Base import message,intersect,SS_VALID
from drg_group.suzhou_2023.DRG import MDCK_DRG

def group(record):
  adrg_zd=["E00.000","E00.000x002","E00.100","E00.100x002","E00.100x003","E00.200","E00.200x002","E00.900","E00.900x002","E00.900x004","E00.900x005","E00.901","E01.000","E01.000x002","E01.000x003","E01.100","E01.100x002","E01.100x003","E01.200","E01.200x001","E01.201","E01.800x002","E01.801","E02.x00","E03.000","E03.000x002","E03.000x004","E03.001","E03.100","E03.100x001","E03.100x002","E03.100x004","E03.101","E03.200x003","E03.201","E03.202","E03.300","E03.400","E03.801","E03.802","E03.900","E03.900x006","E03.901","E04.000","E04.001","E04.100","E04.100x005","E04.101","E04.102","E04.103","E04.104","E04.200","E04.200x001","E04.200x003","E04.201","E04.801","E04.900x001","E04.900x006","E04.901","E04.902","E04.903","E04.904","E05.000","E05.001","E05.003","E05.100","E05.200","E05.200x004","E05.201","E05.202","E05.203","E05.300","E05.301","E05.302","E05.400","E05.400x001","E05.500","E05.800x001","E05.800x005","E05.801","E05.802","E05.804","E05.805","E05.806","E05.900x001","E05.905","E06.000","E06.000x003","E06.001","E06.002","E06.100","E06.100x001","E06.100x002","E06.100x003","E06.100x004","E06.200","E06.300","E06.300x001","E06.300x004","E06.300x005","E06.301","E06.303","E06.304","E06.400","E06.400x002","E06.500x001","E06.500x002","E06.500x004","E06.501","E06.502","E06.900","E07.000","E07.000x001","E07.000x002","E07.001","E07.100","E07.100x002","E07.100x003","E07.800x001","E07.800x003","E07.800x004","E07.800x007","E07.800x009","E07.800x011","E07.801","E07.802","E07.803","E07.804","E07.805","E07.806","E07.901","E15.x00x001","E15.x00x002","E15.x00x004","E16.000x001","E16.100x001","E16.100x002","E16.100x004","E16.100x005","E16.100x006","E16.100x010","E16.100x013","E16.101","E16.102","E16.103","E16.104","E16.105","E16.106","E16.109","E16.110","E16.112","E16.200","E16.300","E16.300x001","E16.300x002","E16.301","E16.800x001","E16.800x002","E16.800x003","E16.800x004","E16.800x006","E16.800x007","E16.800x103","E16.800x104","E16.800x105","E16.800x901","E16.801","E16.802","E16.804","E16.900x002","E16.901","E20.000","E20.100","E20.801","E20.802","E20.900","E20.901","E21.000","E21.000x007","E21.001","E21.002","E21.003","E21.004","E21.005","E21.006","E21.100x001","E21.201","E21.300","E21.300x002","E21.301","E21.400x001","E21.400x003","E21.401","E21.402","E21.500","E22.000x001","E22.000x002","E22.000x005","E22.001","E22.002","E22.100","E22.200","E22.801","E22.802","E22.900","E23.000","E23.000x005","E23.000x007","E23.000x008","E23.000x011","E23.000x014","E23.000x015","E23.001","E23.002","E23.003","E23.004","E23.005","E23.006","E23.007","E23.008","E23.009","E23.010","E23.100","E23.200","E23.200x003","E23.200x005","E23.201","E23.202","E23.203","E23.204","E23.300x001","E23.301","E23.302","E23.600x001","E23.600x005","E23.600x008","E23.600x010","E23.600x011","E23.600x014","E23.600x015","E23.600x016","E23.601","E23.602","E23.603","E23.604","E23.605","E23.606","E23.607","E23.608","E23.610","E23.611","E23.612","E23.613","E23.614","E23.615","E23.616","E23.617","E23.618","E23.619","E23.700x001","E23.701","E24.000","E24.000x001","E24.001","E24.100","E24.200","E24.200x001","E24.201","E24.202","E24.300","E24.400","E24.800x001","E24.801","E24.900","E24.901","E24.902","E25.000x007","E25.000x008","E25.001","E25.002","E25.003","E25.004","E25.005","E25.801","E25.802","E25.901","E25.902","E25.903","E26.000","E26.000x003","E26.001","E26.100","E26.800x002","E26.801","E26.802","E26.803","E26.900","E27.000x001","E27.000x002","E27.000x003","E27.000x011","E27.001","E27.100x003","E27.101","E27.200","E27.200x003","E27.300","E27.400x005","E27.400x006","E27.401","E27.402","E27.403","E27.404","E27.405","E27.406","E27.407","E27.500","E27.500x003","E27.501","E27.800x005","E27.800x010","E27.800x012","E27.800x021","E27.801","E27.802","E27.803","E27.804","E27.805","E27.806","E27.807","E27.808","E27.809","E27.810","E27.901","E30.000","E30.000x003","E30.001","E30.002","E30.100","E30.100x002","E30.101","E30.102","E30.103","E30.801","E31.000","E31.001","E31.002","E31.100","E31.800","E31.900","E31.901","E34.000","E34.100","E34.200","E34.300x002","E34.300x003","E34.300x006","E34.301","E34.302","E34.303","E34.304","E34.305","E34.400","E34.500","E34.500x001","E34.500x002","E34.500x005","E34.501","E34.800x006","E34.801","E34.802","E34.803","E34.804","E34.805","E34.900x003","E34.903","E89.000","E89.001","E89.002","E89.100","E89.101","E89.200x001","E89.201","E89.300x002","E89.300x003","E89.301","E89.302","E89.303","E89.601","E89.801","N25.801","Q85.900x006","Q87.800x911","Q87.807","Q89.100","Q89.101","Q89.200x012","Q89.200x203","Q89.200x204","Q89.201","Q89.203","Q89.205","Q89.206","Q89.207","Q90.000","R94.600","R94.801","S37.803"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合KT1入组条件，匹配规则：主诊断匹配')
    
    if MDCK_DRG.KT11_group(record):
      return 'KT11'

    if MDCK_DRG.KT13_group(record):
      return 'KT13'

    if MDCK_DRG.KT15_group(record):
      return 'KT15'

  return ''

