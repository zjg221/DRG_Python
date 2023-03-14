from drg_group.xian_2020.Base import message,intersect,SS_VALID
from drg_group.xian_2020.DRG import MDCC_DRG

def group(record):
  adrg_zd=["H05.500","H05.500x001","H05.500x002","H11.300","H11.301","H20.802","H21.000","H21.002","H21.003","H26.100x002","H31.000","H31.000x001","H31.000x002","H31.000x004","H31.000x005","H31.300","H31.300x004","H31.301","H31.302","H31.400","H31.400x003","H31.401","H31.402","H31.403","H31.404","H33.200","H33.200x002","H33.200x004","H33.300","H33.300x006","H33.301","H33.302","H33.303","H33.304","H33.400","H33.401","H33.500","H33.500x002","H33.500x006","H33.500x008","H33.501","H33.502","H33.503","H33.504","H33.506","H35.600","H35.601","H35.602","H35.703","H43.100","H44.600","H44.600x002","H44.600x003","H44.600x004","H44.600x005","H44.600x006","H44.600x007","H44.700","H44.700","H44.700x002","H44.700x003","H44.700x004","H44.700x005","H44.700x007","H44.700x008","H44.700x009","H44.801","H59.900","S00.100x001","S00.100x003","S00.100x006","S00.101","S00.200","S00.201","S00.202","S01.000x002","S01.100","S01.101","S01.102","S01.103","S02.311","S02.801","S02.811","S04.000x002","S04.000x003","S04.000x004","S05.000x002","S05.001","S05.002","S05.100x004","S05.101","S05.102","S05.103","S05.104","S05.200x003","S05.200x004","S05.200x005","S05.200x006","S05.200x007","S05.201","S05.202","S05.203","S05.204","S05.205","S05.206","S05.207","S05.208","S05.209","S05.210","S05.300","S05.300x004","S05.300x005","S05.300x010","S05.301","S05.302","S05.303","S05.304","S05.305","S05.306","S05.307","S05.401","S05.500x002","S05.500x003","S05.600x002","S05.601","S05.602","S05.603","S05.604","S05.605","S05.700","S05.800x001","S05.800x007","S05.800x008","S05.800x009","S05.801","S05.802","S05.803","S05.804","S05.805","S05.806","S05.807","S05.808","S05.809","S05.810","S05.811","S05.812","S05.900","S05.900x003","S05.901","S05.902","S05.903","T15.000","T15.100x001","T15.101","T15.800x001","T15.800x002","T15.801","T15.900","T20.000x012","T26.000","T26.001","T26.002","T26.100x001","T26.100x003","T26.101","T26.102","T26.200x001","T26.301","T26.400","T26.400x001","T26.401","T26.500","T26.500x002","T26.500x003","T26.600x001","T26.600x002","T26.600x003","T26.601","T26.602","T26.603","T26.604","T26.605","T26.700x001","T26.800x001","T26.900","T26.900x001","T26.901","T26.902","T85.200","T85.200x001","T85.200x002","T85.201","T85.202","T85.300x001","T85.300x003","T85.300x004","T85.300x005","T85.300x006","T85.300x007","T85.300x008","T85.300x009","T85.301","T85.302","T85.303","T85.304","T85.308","T85.309","T85.310","T85.311","T85.312"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合CT1入组条件，匹配规则：主诊断匹配')
    
    if MDCC_DRG.CT11_group(record):
      return 'CT11'

    if MDCC_DRG.CT13_group(record):
      return 'CT13'

    if MDCC_DRG.CT15_group(record):
      return 'CT15'

    return 'CT1'
  else:
    return ''

