from drg_group.lanzhou_2023.Base import message,intersect,SS_VALID
from drg_group.lanzhou_2023.DRG import MDCJ_DRG

def group(record):
  adrg_zd=["D17.000x004","D17.100x001","D17.100x002","D17.100x003","D17.101","D17.200x001","D17.200x002","D17.200x003","D17.200x004","D17.200x005","D17.300x001","D17.300x002","D17.300x004","D17.300x005","D17.301","D17.500x010","D17.500x011","D17.900x001","D17.900x002","D18.000x010","D18.000x018","D18.000x847","D18.000x848","D18.000x849","D18.000x850","D18.000x851","D18.000x852","D18.005","D18.006","D18.007","D18.008","D22.500","D22.500x008","D22.501","D22.502","D22.503","D22.504","D22.505","D22.506","D22.507","D22.508","D22.509","D22.510","D22.511","D22.600","D22.601","D22.602","D22.700","D22.701","D22.702","D22.900","D22.900x002","D22.900x003","D22.900x017","D22.900x021","D23.400x003","D23.401","D23.500","D23.500x003","D23.500x006","D23.500x010","D23.501","D23.503","D23.504","D23.505","D23.506","D23.600x001","D23.600x002","D23.601","D23.602","D23.700x001","D23.700x002","D23.701","D23.900","D28.000x001","D36.700x009","D36.716","D48.501","D48.503","D48.505","D48.509","D48.511","D48.513","D48.515","D48.517","D86.300","D86.300x002","E05.906","I89.800x012","I89.800x013","I89.800x014","I89.800x015","I89.800x020","I89.800x022","I89.800x024","I89.800x025","I89.800x026","I89.800x027","I89.800x028","I89.800x029","I89.800x030","L90.500x006","L90.500x007","L90.500x008","L90.500x009","L90.500x010","L90.500x011","L90.500x012","L90.500x013","L90.500x014","L90.500x015","L90.500x016","L90.500x017","L90.500x018","L90.500x019","L90.500x020","L90.500x021","L90.500x022","L90.500x023","L90.500x024","L90.500x025","L90.500x026","L90.500x027","L90.500x028","L90.500x029","L90.500x030","L90.500x031","L90.500x032","L90.500x033","L90.500x034","L90.500x035","L90.500x036","L90.500x037","L90.500x038","L90.500x039","L90.500x040","L90.500x041","L90.500x042","L90.500x043","L90.500x044","L90.500x045","L90.500x046","L90.500x047","L90.500x048","L90.500x049","L90.500x050","L90.500x051","L90.500x052","L90.500x053","L90.500x054","L90.500x055","L90.500x056","L90.500x057","L90.500x058","L90.500x059","L90.500x060","L90.500x061","L90.500x062","L90.500x063","L90.500x064","L90.500x065","L90.500x066","L90.500x067","L90.500x071","L90.500x072","L90.500x073","L90.500x074","L90.501","L90.502","L90.503","L90.504","L90.505","L90.800","L91.001","L91.801","L92.200","L92.800","L92.901","L92.903","M79.801","M79.802","M79.803","M79.804","M79.805","M79.806","M79.807","M79.811","R22.000x003","R22.000x004","R22.000x005","R22.002","R22.003","R22.004","R22.005","R22.006","R22.100x001","R22.100x002","R22.200x001","R22.200x002","R22.200x004","R22.202","R22.203","R22.204","R22.205","R22.206","R22.207","R22.300x001","R22.300x002","R22.302","R22.400x002","R22.400x003","R22.402","R22.700x001","R22.700x002","R22.901","R22.902","R22.903","R22.904"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合JV1入组条件，匹配规则：主诊断匹配')
    
    if MDCJ_DRG.JV1A_group(record):
      return 'JV12'

    if MDCJ_DRG.JV15_group(record):
      return 'JV15'

    return 'JV1'
  else:
    return ''

