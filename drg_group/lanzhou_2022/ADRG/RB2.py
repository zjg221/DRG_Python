from drg_group.lanzhou_2022.Base import message,intersect,SS_VALID
from drg_group.lanzhou_2022.DRG import MDCR_DRG

def group(record):
  adrg_zd=["C81.000","C81.100","C81.200","C81.300","C81.400","C81.700","C81.701","C81.702","C81.703","C81.900","C81.900x005","C82.000","C82.100","C82.200","C82.300","C82.400","C82.500","C82.600","C82.700","C82.701","C82.702","C82.703","C82.704","C82.900","C82.901","C82.903","C83.000","C83.001","C83.002","C83.003","C83.004","C83.100","C83.101","C83.102","C83.300","C83.300x006","C83.300x007","C83.300x008","C83.300x009","C83.301","C83.302","C83.303","C83.304","C83.305","C83.306","C83.307","C83.500","C83.501","C83.502","C83.503","C83.504","C83.505","C83.700","C83.702","C83.703","C83.800","C83.800x006","C83.800x008","C83.800x009","C83.801","C83.802","C83.803","C83.900","C84.000","C84.000x002","C84.000x003","C84.100","C84.400","C84.400x001","C84.401","C84.402","C84.403","C84.404","C84.405","C84.406","C84.407","C84.500","C84.500x004","C84.500x012","C84.500x016","C84.502","C84.600","C84.601","C84.700","C84.800","C84.900","C84.901","C85.100","C85.100x010","C85.100x017","C85.100x021","C85.200","C85.700","C85.700x004","C85.700x016","C85.701","C85.704","C85.705","C85.707","C85.709","C85.715","C85.900","C85.900x001","C85.900x002","C85.900x003","C85.900x004","C85.900x005","C85.900x006","C85.900x008","C85.900x009","C85.900x010","C85.900x011","C85.900x012","C85.900x013","C85.900x014","C85.900x015","C85.900x016","C85.900x017","C85.900x019","C85.900x020","C85.900x022","C85.900x023","C85.900x024","C85.900x025","C85.900x026","C85.900x027","C85.900x028","C85.900x029","C85.900x030","C85.900x031","C85.900x034","C85.900x036","C85.900x037","C85.900x038","C85.900x039","C85.900x040","C85.900x041","C85.900x042","C85.900x043","C85.901","C86.000","C86.100","C86.200","C86.300","C86.400","C86.500","C86.600","C86.601","C86.602","C86.603","C90.000","C90.000x004","C90.000x005","C90.000x008+M90.6*","C90.000x009","C90.000x011","C90.000x012","C90.000x014","C90.000x021","C90.000x022","C90.000x023","C90.000x024","C90.000x025","C90.000x026","C90.000x027","C90.000x028","C90.000x029","C90.000x030","C90.000x031","C90.000x032","C90.000x033","C90.000x034","C90.000x035","C90.000x036","C90.000x037","C90.000x038","C90.000x039","C90.000x040","C90.000x041","C90.001","C90.002","C90.004+N16.1*","C90.005+N08.1*","C90.100","C90.100x002","C90.100x011","C90.200","C90.200x008","C90.200x009","C90.200x013","C90.300","C90.300x001","C90.300x002","C90.300x003","C90.300x004","C90.301","C90.302","C90.303"]
  adrg_zd1=[]
  adrg_ss=["00.1500x001","00.1500x002","99.2500x017","99.2500x036","99.2500x037","99.2502","99.2503","99.2504","99.2505","99.2506","99.2800x003","99.2801"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss:
    message('符合RB2入组条件，匹配规则：主诊断匹配、主手术匹配')
    
    if MDCR_DRG.RB21_group(record):
      return 'RB21'

    if MDCR_DRG.RB2B_group(record):
      return 'RB24'

    return 'RB2'
  else:
    return ''

