from drg_group.changzhou_2022.Base import message,intersect,SS_VALID
from drg_group.changzhou_2022.DRG import MDCN_DRG

def group(record):
  adrg_zd=["C45.100","C46.700x001","C51.000","C51.001","C51.100","C51.200","C51.800","C51.900","C52.x00","C53.000","C53.100","C53.800","C53.801","C53.900","C54.000","C54.001","C54.100","C54.200","C54.300","C54.800","C54.900","C55.x00","C56.x00","C56.x00x003","C57.000","C57.000x002","C57.100","C57.101","C57.200","C57.300","C57.300x001","C57.301","C57.400","C57.700","C57.701","C57.702","C57.800x004","C57.800x005","C57.801","C57.802","C57.803","C57.900","C58.x00","C58.x00x002","C58.x00x003","C76.307","C77.500x003","C79.600","C79.800x202","C79.800x205","C79.800x206","C79.800x209","C79.800x211","C79.800x213","C79.800x214","C79.800x215","C79.800x216","C79.800x218","C79.800x219","C79.800x220","C79.800x222","C79.800x223","C79.812","C79.813","C79.814","C79.822","C79.823","C79.833","D39.000x001","D39.000x002","D39.100x003","D39.200x001","D39.200x002","D39.201","D39.202","D39.203","D39.204","D39.700x001","D39.700x002","D39.900x001"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合NR1入组条件，匹配规则：主诊断匹配')
    
    if MDCN_DRG.NR11_group(record):
      return 'NR11'

    if MDCN_DRG.NR13_group(record):
      return 'NR13'

    if MDCN_DRG.NR15_group(record):
      return 'NR15'

    return 'NR1'
  else:
    return ''

