from drg_group.yancheng_2023.Base import message,intersect,SS_VALID
from drg_group.yancheng_2023.DRG import MDCC_DRG

def group(record):
  adrg_zd=["E10.300x051+H42.0*","E11.300x051+H42.0*","H40.000","H40.000x001","H40.000x002","H40.000x004","H40.001","H40.100","H40.100x001","H40.100x004","H40.101","H40.103","H40.200","H40.200x006","H40.200x007","H40.200x009","H40.200x010","H40.200x011","H40.200x012","H40.202","H40.203","H40.300","H40.300","H40.400","H40.401","H40.403","H40.500","H40.500x002","H40.500x008","H40.500x009","H40.501","H40.502","H40.503","H40.504","H40.505","H40.506","H40.600","H40.600x002","H40.800x002","H40.800x004","H40.800x005","H40.801","H40.900","H44.501","H59.800x004","H59.800x007","H59.801","H59.808","H59.809","Q13.101+H42.8*","Q15.000","Q15.003","Q15.004","Q15.005","Z03.801"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合CV1入组条件，匹配规则：主诊断匹配')
    
    if MDCC_DRG.CV19_group(record):
      return 'CV19'

    return 'CV1'
  else:
    return ''

