from drg_group.wlmq_2022.Base import message,intersect,SS_VALID
from drg_group.wlmq_2022.DRG import MDCB_DRG

def group(record):
  adrg_zd=["G10.x00x004","G10.x00x005","G95.001","H47.203","Q00.100","Q00.200x101","Q00.200x201","Q01.000","Q01.100","Q01.200","Q01.800x101","Q01.800x201","Q01.800x301","Q01.800x401","Q01.801","Q01.900","Q01.900x001","Q01.900x003","Q01.901","Q02.x00","Q03.001","Q03.002","Q03.101","Q03.102","Q03.103","Q03.800","Q03.900","Q04.000","Q04.000x011","Q04.100","Q04.200","Q04.300x011","Q04.300x021","Q04.300x031","Q04.300x502","Q04.301","Q04.302","Q04.303","Q04.304","Q04.305","Q04.306","Q04.307","Q04.400","Q04.500","Q04.600","Q04.600x202","Q04.601","Q04.602","Q04.603","Q04.604","Q04.800x002","Q04.800x003","Q04.800x005","Q04.801","Q04.802","Q04.803","Q04.900","Q04.902","Q05.000","Q05.000x002","Q05.100","Q05.100x002","Q05.200","Q05.200x002","Q05.300","Q05.300x002","Q05.400","Q05.400x001","Q05.500","Q05.500x002","Q05.600","Q05.600x002","Q05.700","Q05.700x002","Q05.700x003","Q05.700x004","Q05.700x005","Q05.800","Q05.801","Q05.900","Q05.900x002","Q05.900x006","Q05.900x007","Q05.901","Q05.902","Q06.000","Q06.100","Q06.101","Q06.200","Q06.400","Q06.400x002","Q06.800x002","Q06.800x003","Q06.800x005","Q06.801","Q06.900","Q06.901","Q07.000","Q07.800","Q07.800x202","Q07.800x901","Q07.800x902","Q07.800x903","Q07.800x904","Q07.801","Q25.800x003","Q27.800x032","Q27.801","Q27.819","Q28.000","Q28.001","Q28.100","Q28.103","Q28.104","Q28.105","Q28.106","Q28.200","Q28.200x006","Q28.201","Q28.202","Q28.203","Q28.300x001","Q28.300x005","Q28.300x007","Q28.301","Q28.302","Q28.303","Q28.304","Q28.305","Q28.800x004","Q28.800x006","Q76.000","Q85.805","Q85.910"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合BW1入组条件，匹配规则：主诊断匹配')
    
    if MDCB_DRG.BW19_group(record):
      return 'BW19'

    return 'BW1'
  else:
    return ''

