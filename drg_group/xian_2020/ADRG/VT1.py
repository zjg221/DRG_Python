from drg_group.xian_2020.Base import message,intersect,SS_VALID
from drg_group.xian_2020.DRG import MDCV_DRG

def group(record):
  adrg_zd=["N99.400","N99.401","N99.900","T80.100x001","T80.100x002","T80.200x003","T80.604","T80.900","T80.902","T81.000x001","T81.000x002","T81.000x004","T81.000x005","T81.000x009","T81.000x010","T81.000x011","T81.000x013","T81.000x014","T81.000x018","T81.000x019","T81.000x020","T81.000x021","T81.000x022","T81.000x023","T81.000x024","T81.000x026","T81.000x027","T81.000x028","T81.000x029","T81.000x030","T81.000x031","T81.000x032","T81.000x033","T81.000x034","T81.000x035","T81.000x036","T81.000x037","T81.000x038","T81.000x039","T81.000x041","T81.000x042","T81.001","T81.002","T81.003","T81.004","T81.005","T81.006","T81.007","T81.008","T81.009","T81.010","T81.011","T81.012","T81.013","T81.014","T81.015","T81.016","T81.017","T81.018","T81.019","T81.020","T81.021","T81.022","T81.023","T81.024","T81.025","T81.026","T81.027","T81.028","T81.029","T81.030","T81.031","T81.032","T81.033","T81.034","T81.035","T81.036","T81.101","T81.102","T81.200x001","T81.200x002","T81.200x005","T81.200x009","T81.200x010","T81.200x012","T81.200x013","T81.200x014","T81.200x015","T81.200x016","T81.200x017","T81.201","T81.202","T81.203","T81.204","T81.205","T81.206","T81.207","T81.208","T81.209","T81.210","T81.211","T81.212","T81.213","T81.214","T81.215","T81.216","T81.217","T81.218","T81.219","T81.220","T81.221","T81.301","T81.400x007","T81.400x008","T81.400x009","T81.400x010","T81.400x011","T81.400x012","T81.400x013","T81.400x014","T81.407","T81.408","T81.409","T81.411","T81.412","T81.500x001","T81.500x002","T81.500x006","T81.500x007","T81.501","T81.502","T81.503","T81.504","T81.505","T81.600x001","T81.700x106","T81.700x107","T81.700x108","T81.700x206","T81.700x207","T81.700x208","T81.700x305","T81.700x306","T81.700x307","T81.700x406","T81.700x407","T81.700x408","T81.800x001","T81.800x002","T81.800x003","T81.800x004","T81.800x005","T81.800x017","T81.801","T81.804","T81.805","T81.806","T81.807","T81.808","T81.809","T81.810","T81.811","T81.812","T81.813","T81.900","T83.900","T84.200x004","T85.500","T85.500x001","T85.500x002","T85.500x003","T85.501","T85.600","T85.600x001","T85.600x003","T85.600x004","T85.600x006","T85.600x007","T85.600x008","T85.600x009","T85.600x010","T85.601","T85.602","T85.603","T85.604","T85.606","T85.607","T85.608","T85.609","T85.610","T85.611","T85.700","T85.700x804","T85.704","T85.705","T85.800x801","T85.800x803","T85.803","T85.900","T85.901","T86.800x805","T86.800x807","T86.800x808","T86.800x809","T86.800x813","T86.800x814","T86.805","T86.806","T86.808","T88.100x002","T88.101","T88.200","T88.300","T88.400x001","T88.400x002","T88.501","T88.702","T88.800x001","T88.900","T98.200x033","T98.300x002","T98.300x003","T98.300x004","T98.300x005","T98.300x006"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合VT1入组条件，匹配规则：主诊断匹配')
    
    if MDCV_DRG.VT11_group(record):
      return 'VT11'

    if MDCV_DRG.VT13_group(record):
      return 'VT13'

    if MDCV_DRG.VT15_group(record):
      return 'VT15'

    return 'VT1'
  else:
    return ''

