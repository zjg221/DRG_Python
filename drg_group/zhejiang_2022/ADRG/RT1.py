from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCR_DRG

def group(record):
  adrg_zd=["C45.100","C45.100x005","C45.103","C45.700x002","C45.706","C45.900","C46.100","C46.300","C46.700","C46.800","C46.900","C46.900x002","C46.900x003","C46.900x004","C48.000","C48.000x002","C48.100","C48.100x006","C48.103","C48.104","C48.105","C48.200","C48.201","C48.800","C49.901","C75.400","C76.100","C76.100x003","C76.101","C76.200","C76.200x002","C76.300","C76.300x001","C76.300x009","C76.301","C76.302","C76.304","C76.305","C76.306","C76.307","C76.400","C76.401","C76.402","C76.500","C76.501","C76.502","C76.503","C76.700","C76.700x002","C76.701","C76.702","C76.800","C76.801","C77.107","C77.200","C77.205","C77.206","C77.300","C77.300x001","C77.300x003","C77.301","C77.302","C77.303","C77.400x001","C77.401","C77.500","C77.501","C77.502","C77.503","C77.800","C77.900","C77.900x001","C78.201","C78.600x004","C78.601","C78.602","C78.604","C78.605","C79.800x804","C79.800x809","C79.800x811","C79.800x813","C79.800x816","C79.800x817","C79.800x818","C79.800x834","C79.800x837","C79.800x838","C79.800x862","C79.807","C79.809","C79.811","C79.821","C79.824","C79.826","C79.827","C79.829","C79.900","C79.900x001","C80.000","C80.000x001","C80.001","C80.004+G73.1*","C80.900","C80.901","C80.902","C80.903","C80.904","C80.905","C90.000x008+M90.6*","C96.500","C96.501","C96.502","C96.600","C96.601","C96.602","C96.603","C96.604","C97.x00","C97.x01","D09.700","D09.700x001","D09.700x002","D09.900","D38.300x001","D38.300x002","D38.300x003","D38.301","D44.601","D44.700x002","D44.701","D44.703","D48.100x008","D48.300x001","D48.301","D48.400x002","D48.400x003","D48.401","D48.700x001","D48.700x004","D48.700x005","D48.700x010","D48.700x013","D48.700x015","D48.700x016","D48.700x019","D48.700x023","D48.707","D48.708","D48.709","D48.710","D48.713","D48.714","D48.715","D48.716","D48.717","D48.718","D48.719","D48.720","D48.721","D48.722","D48.723","D48.724","D48.725","D48.900","D48.901","D48.902","Q85.801","Q85.802","Q85.806","R58.x00x005","R58.x00x007","Z51.800x092","Z51.800x097","Z51.800x921"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合RT1入组条件，匹配规则：主诊断匹配')
    
    if MDCR_DRG.RT11_group(record):
      return 'RT11'

    if MDCR_DRG.RT13_group(record):
      return 'RT13'

    if MDCR_DRG.RT15_group(record):
      return 'RT15'

    return 'RT1'
  else:
    return ''

