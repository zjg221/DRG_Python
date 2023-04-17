from drg_group.yantai_2023.Base import message,intersect,SS_VALID
from drg_group.yantai_2023.DRG import MDCJ_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["08.2000x003","08.2000x005","08.2000x006","08.2000x009","08.2000x010","08.2001","08.2300x001","08.2400x001","08.2500","08.3101","08.3200x001","08.3200x002","08.3200x003","08.3300x001","08.3600x002","08.3700","08.3800","08.4102","08.4202","08.4203","08.4301","08.4401","08.4402","08.4901","08.4902","08.5100","08.5101","08.5200x002","08.5200x003","08.5200x004","08.5900x001","08.5900x004","08.5900x005","08.5900x006","08.5900x007","08.5901","08.5902","08.5903","08.5904","08.6100x002","08.6100x003","08.6100x004","08.6101","08.6201","08.6400","08.7001","08.7100x001","08.7200x001","08.7300x001","08.7400x001","08.8101","08.8102","08.8200x001","08.8300x001","08.8400x001","08.8500x001","08.8600x002","08.8700","08.8900x002","08.8900x005","08.8901","08.8902","08.9900x003","08.9901","18.4x00","18.5x00x001","18.6x00x001","18.6x01","18.6x02","18.7100x001","18.7100x002","18.7100x009","18.7100x010","18.7101","18.7102","18.7104","18.7105","18.7200","18.7900x002","18.7900x008","18.7900x009","18.7901","18.7902","18.7905","18.7906","18.9x00x002","18.9x00x004","18.9x00x005","18.9x00x007","21.8300x001","21.8301","21.8302","21.8400x002","21.8400x003","21.8400x006","21.8401","21.8402","21.8500x002","21.8500x004","21.8500x005","21.8500x007","21.8500x008","21.8500x010","21.8500x011","21.8501","21.8502","21.8503","21.8504","21.8505","21.8600x004","21.8601","21.8602","21.8603","21.8700x003","21.8700x004","21.8700x005","21.8700x008","21.8700x009","21.8701","21.8702","21.8801","21.8802","27.5100","27.5200","27.5301","27.5302","27.5303","27.5401","27.5700x005","27.5701","27.5702","27.5703","27.5900x011","27.5900x017","27.5900x018","27.5900x019","27.5900x020","27.5901","27.5902","27.5903","27.5904","27.5906","27.5907","27.5909","27.5910","27.5911","27.5912","27.5913","27.5914","27.5915","27.6200x002","27.6200x003","27.6201","27.6300x002","27.6301","27.6302","27.6400","27.6900x003","27.6900x004","27.6900x007","27.6900x008","27.6901","27.6902","27.6903","27.6904","27.6905","27.6906","27.6907","27.6908","27.6909","27.7202","27.9100x001","27.9101","27.9900x001","27.9900x005","27.9900x006","27.9900x007","27.9900x009","27.9903","27.9904","86.6400x002","86.6400x003","86.8100x002","86.8100x003","86.8100x004","86.8100x005","86.8100x006","86.8200x006","86.8200x007","86.8200x008","86.8200x009","86.8200x010","86.8200x011","86.8201","86.8202","86.8203","86.8300x031","86.8300x032","86.8300x034","86.8300x035","86.8301","86.8302","86.8303","86.8304","86.8305","86.8306","86.8700x001","86.8701","86.8702","86.8900x002","86.8900x010","86.8900x011","86.8900x014","86.8901","86.8902"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合JC1入组条件，匹配规则：主手术匹配')
    
    if MDCJ_DRG.JC19_group(record):
      return 'JC19'

    return 'JC1'
  else:
    return ''

