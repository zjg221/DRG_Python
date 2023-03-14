from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCV_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["00.6200x005","00.6201","00.6202","00.8500x001","00.8600x001","00.8700x001","04.0420","04.4910","04.7400x032","04.7502","07.8000","07.8001","07.8100","07.8100x009","07.8201","07.8300","07.8300x002","07.8400","07.8401","07.9100","07.9200x001","07.9300","07.9400","07.9500","07.9800","07.9901","08.2000x006","08.2001","08.2100x004","08.2200x003","08.2201","08.2300x001","08.2400x001","08.2500","08.3101","08.3200x001","08.3200x002","08.3600x002","08.4102","08.4202","08.4203","08.4301","08.4401","08.4402","08.4901","08.4902","08.5101","08.5200x002","08.5200x003","08.5900x001","08.5900x004","08.5900x005","08.5901","08.6100x002","08.6100x003","08.6100x004","08.6201","08.7100x001","08.7200x001","08.7300x001","08.7400x001","08.8101","08.8102","08.8200x001","08.8300x001","08.8400x001","08.8500x001","08.8900x005","09.2200x001","09.2300","09.4402","09.4404","09.5200","09.6x00x006","09.6x01","09.7100","09.7300x001","09.7300x004","09.7301","09.8100x004","09.8101","09.8200","09.8301","10.0x00x001","10.1x00x002","10.2900x001","10.3101","10.3102","10.3200","10.3201","10.3300x002","10.3301","10.3302","10.4100x001","10.4101","10.4102","10.4200x001","10.4201","10.4202","10.4300x002","10.4400x001","10.4401","10.4402","10.4403","10.4900x001","10.4900x003","10.4901","10.4903","10.4904","10.6x00x001","10.6x00x002","11.0x00","11.1x01","11.3201","11.3202","11.3203","11.3204","11.3901","11.4200","11.4300","11.4901","11.4902","11.4903","11.5100","11.5101","11.5200","11.5300x001","11.5900x001","11.5900x002","11.5901","11.6000x002","11.6000x003","11.6100","11.6200x002","11.6200x003","11.6300x001","11.6300x002","11.6400x001","11.6400x002","11.6900x001","11.6900x002","11.6900x003","11.6901","11.6902","11.7100x001","11.7100x002","11.7101","11.7102","11.7103","11.7104","11.7200x005","11.7300x001","11.7400x001","11.7500","11.7600","11.7900x001","11.7901","11.7902","11.7904","11.9100x001","11.9200x001","11.9900x001","11.9900x002","11.9901","12.0000","12.0100","12.0200x002","12.0200x003","12.0200x004","12.1100x002","12.1101","12.1200x001","12.1201","12.1202","12.1203","12.1300","12.1400x001","12.1400x008","12.1401","12.1402","12.1403","12.1404","12.3100","12.3200x001","12.3300","12.3301","12.3400","12.3500","12.3502","12.3503","12.3504","12.3505","12.3900x001","12.3900x004","12.3901","12.3902","12.4000","12.4100x001","12.4201","12.4300x001","12.4401","12.5200x001","12.5300","12.5400","12.5501","12.5900x001","12.5900x003","12.5901","12.6100","12.6200","12.6301","12.6400x001","12.6400x003","12.6400x009","12.6400x010","12.6401","12.6402","12.6403","12.6404","12.6405","12.6406","12.6407","12.6408","12.6500x003","12.6500x004","12.6501","12.6502","12.6503","12.6601","12.6703","12.6901","12.7401","12.7901","12.7904","12.8100","12.8200x001","12.8300x002","12.8302","12.8303","12.8304","12.8400x002","12.8400x004","12.8401","12.8402","12.8403","12.8404","12.8500x002","12.8600x001","12.8701","12.8702","12.8703","12.8800x002","12.8801","12.8802","12.8900x001","12.8900x007","12.8901","12.8902","12.8903","12.8904","12.9100x002","12.9100x004","12.9301","12.9302","12.9701","12.9702","12.9703","12.9801","12.9802","12.9803","12.9900x004","12.9901","12.9903","13.0100","13.0201","14.0000","14.0101","14.0200x001","14.0200x002","14.0201","14.0202","14.2301","14.2403","14.2500","14.2601","14.2602","14.2700x001","14.2900x003","14.2900x004","14.2901","14.2902","14.3101","14.3200x002","14.3300","14.3500","14.3901","14.4100","14.4900x001","14.4901","14.4902","14.4903","14.5101","14.5200x001","14.5300x001","14.5400x001","14.5500","14.5901","14.5902","14.5903","14.5904","14.6x00x001","14.6x01","14.6x02","14.7100x001","14.7202","14.7203","14.7300x001","14.7401","14.7500x002","14.7501","14.7901","14.7902","14.7904","14.7905","14.9x00x001","14.9x01","14.9x02","14.9x03","14.9x05","14.9x06","14.9x07","14.9x08","15.7x01","15.9x00x001","15.9x00x007","15.9x01","16.0101","16.0900x004","16.0900x005","16.0901","16.0904","16.1x00x001","16.1x01","16.1x02","16.4900x001","16.5200","16.5900x001","16.5901","16.5902","16.6100x001","16.6101","16.6200x001","16.6300x002","16.6500","16.7101","16.7200","16.8100x002","16.8200","16.8900x001","16.8900x002","16.8901","16.8902","16.8903","16.8904","16.9201","16.9300x003","18.3900x003","18.3901","18.4x00","18.6x00x001","18.6x01","18.6x02","18.7100x001","18.7100x002","18.7100x009","18.7100x010","18.7101","18.7102","18.7104","18.7105","18.7200","18.7900x008","18.7900x009","18.7901","18.7902","18.7906","18.9x00x002","18.9x00x004","18.9x00x005","21.0400","21.0500","21.0600","21.0700x001","21.0901","21.4x00","21.5x00","21.5x00x004","21.5x01","21.7100","21.7200","21.7200x001","21.8100","21.8400x002","21.8400x003","21.8400x006","21.8500x002","21.8500x004","21.8500x005","21.8500x007","21.8500x008","21.8500x010","21.8500x011","21.8501","21.8502","21.8503","21.8504","21.8505","21.8600x004","21.8603","21.8700x003","21.8700x004","21.8700x005","21.8700x008","21.8700x009","21.8701","21.8702","21.8801","21.8802","21.8900x002","21.8900x003","21.8900x004","21.8901","21.9900x005","21.9901","24.2x00","24.3101","24.5x00x003","24.5x03","25.5100x001","25.5900x008","25.5900x009","25.5900x010","25.5900x011","25.5902","25.5903","25.5904","25.5905","25.5906","26.4100x001","26.4200x001","26.4200x002","26.4900x001","26.4900x005","26.4900x006","26.4900x007","26.4900x008","26.4900x009","26.4900x010","26.4901","26.4902","27.0x01","27.0x02","27.0x03","27.0x04","27.0x05","27.0x06","27.0x08","27.0x09","27.0x10","27.0x11","27.3104","27.3201","27.3202","27.3203","27.4900x007","27.4900x009","27.4900x014","27.4900x018","27.4900x019","27.4901","27.4902","27.4903","27.4904","27.4905","27.4906","27.4907","27.4908","27.4909","27.4910","27.5100","27.5301","27.5302","27.5303","27.5401","27.5500x002","27.5600x002","27.5601","27.5700x005","27.5701","27.5702","27.5703","27.5900x011","27.5901","27.5902","27.5903","27.5904","27.6100","27.9900x001","27.9900x005","27.9900x006","27.9900x007","27.9900x009","27.9900x010","27.9901","27.9902","27.9903","29.5100","29.5300x002","29.5301","29.5302","29.5901","30.1x00","30.2100","30.2100x002","30.2100x003","30.2101","30.2200","30.2201","30.2202","30.2203","30.2204","30.2900x001","30.2900x002","30.2900x003","30.2900x009","30.2904","30.3x04","31.6100","31.6201","31.6202","31.6400","31.6900x007","31.6900x008","31.6900x013","31.6901","31.6902","31.6903","31.6904","31.6905","31.6906","31.6907","31.6908","31.6909","31.6910","31.6911","31.6912","31.6913","31.7100x001","31.7300x001","31.7301","31.7500x002","31.7500x004","31.7501","31.7502","31.7503","31.7504","31.7900x004","31.7900x005","31.7900x006","31.7901","31.7902","31.7903","31.7904","31.9201","31.9202","31.9203","31.9204","31.9500","31.9501","31.9901","31.9902","31.9903","31.9904","31.9905","32.1x00x004","32.1x01","32.1x02","32.2000x002","32.2001","32.2201","32.2900x016","32.2901","32.2902","32.2903","32.2904","32.2905","32.3001","32.3900x003","32.3901","32.3902","32.4100","32.4100x002","32.4900x002","32.4900x003","32.4901","32.4902","32.4903","32.5000x001","32.5900x001","33.0x00x003","33.0x00x004","33.0x03","33.1x00x003","33.1x00x004","33.1x04","33.4100","33.4100x002","33.4200x001","33.4300x002","33.4801","33.4802","33.4803","33.4804","33.4805","33.4901","33.4902","33.9200","33.9900x001","33.9901","33.9902","34.0103","34.0200x001","34.0200x003","34.0300x001","34.0301","34.0900x006","34.0900x011","34.0903","34.0904","34.0906","34.1x01","34.1x02","34.1x03","34.1x04","34.2100x001","34.2200","34.5101","34.5901","34.5902","34.5903","34.5904","34.6x00","34.6x01","34.6x02","34.7100","34.7200","34.7300x001","34.7301","34.7302","34.7303","34.7900x001","34.7900x002","34.7900x003","34.7900x004","34.8200","34.8200x002","34.8301","34.8302","34.8303","34.8400x003","34.8500","34.8900x002","34.8900x003","34.8900x004","34.9300","34.9301","34.9302","34.9901","34.9902","34.9904","34.9905","37.1100x004","37.1100x005","37.1101","37.1102","37.1103","37.1200x005","37.1202","37.1203","37.1204","37.3101","37.3102","37.3103","37.4900x001","37.4900x002","37.4900x005","37.4903","37.7200","37.7300","37.7401","37.7402","37.7501","37.7600x002","37.7701","37.7800","37.7900x003","37.7900x004","37.8000x001","37.8300x002","37.8700x002","37.9100","37.9901","38.0200x002","38.0200x003","38.0201","38.0300x003","38.0300x005","38.0301","38.0302","38.0400x001","38.0500x002","38.0501","38.0502","38.0503","38.0600x001","38.0602","38.0700x001","38.0700x003","38.0702","38.0703","38.0704","38.0800x002","38.0800x003","38.0801","38.0900x001","38.0900x002","38.0901","38.0902","38.1000x002","38.1200x003","38.1201","38.1202","38.1400x001","38.1401","38.1402","38.1500x001","38.1501","38.1600x002","38.1600x005","38.1601","38.1602","38.1603","38.1800x001","38.1800x002","38.1800x003","38.1800x004","38.1800x005","38.1800x006","38.1800x007","38.1801","38.1802","38.1803","38.1804","38.3000","38.3100","38.3100x001","38.3101","38.3202","38.3501","38.3800","38.4200x001","38.4200x002","38.4200x003","38.4300x002","38.4400x001","38.4500x001","38.4500x003","38.4500x010","38.4500x011","38.4500x013","38.4500x014","38.4503","38.4506","38.4600x001","38.4700x001","38.4701","38.4702","38.4900x001","38.4900x002","38.6302","38.6700x003","38.6701","38.6702","38.6704","38.6800x002","38.6801","38.6802","38.6901","38.7x01","38.7x02","38.7x03","38.7x04","38.8100x004","38.8101","38.8200x003","38.8200x005","38.8200x006","38.8200x007","38.8200x008","38.8202","38.8203","38.8300x004","38.8301","38.8302","38.8303","38.8500x001","38.8500x010","38.8500x012","38.8500x013","38.8500x016","38.8501","38.8502","38.8503","38.8504","38.8600x004","38.8600x005","38.8601","38.8602","38.8603","38.8604","38.8605","38.8606","38.8607","38.8609","38.8700x001","38.8700x002","38.8700x008","38.8700x009","38.8701","38.8702","38.8704","38.8800x002","38.8801","38.8900x001","38.8901","39.2200x001","39.2200x002","39.2200x003","39.2200x004","39.2200x005","39.2200x006","39.2200x008","39.2200x009","39.2200x010","39.2200x011","39.2200x012","39.2200x014","39.2200x015","39.2200x016","39.2200x017","39.2200x018","39.2200x019","39.2200x021","39.2300x003","39.2401","39.2500x001","39.2500x002","39.2500x003","39.2500x004","39.2500x005","39.2500x006","39.2500x007","39.2500x008","39.2500x009","39.2500x010","39.2500x011","39.2500x012","39.2500x013","39.2600x001","39.2600x002","39.2600x003","39.2600x004","39.2600x006","39.2600x007","39.2600x008","39.2600x009","39.2600x010","39.2605","39.2700x001","39.2700x002","39.2700x003","39.2700x004","39.2800x002","39.2801","39.2900x001","39.2900x002","39.2900x003","39.2900x004","39.2900x005","39.2900x010","39.2900x011","39.2900x012","39.2900x015","39.2900x017","39.2900x019","39.2900x024","39.2900x025","39.2900x026","39.2900x027","39.2900x028","39.2900x030","39.2900x031","39.2900x032","39.2900x033","39.2900x034","39.2900x035","39.2900x036","39.2900x037","39.2900x038","39.2900x039","39.2900x040","39.2900x041","39.2900x042","39.2900x043","39.2900x044","39.2900x045","39.2900x046","39.2900x047","39.2900x048","39.2900x049","39.2902","39.2906","39.2907","39.2908","39.2915","39.2916","39.3100x002","39.3100x004","39.3100x005","39.3100x006","39.3100x007","39.3100x009","39.3100x010","39.3200x004","39.3200x006","39.3201","39.3203","39.3206","39.3207","39.4901","39.5000x011","39.5000x013","39.5000x014","39.5000x015","39.5000x019","39.5000x021","39.5000x024","39.5000x025","39.5000x026","39.5000x027","39.5000x029","39.5000x030","39.5001","39.5002","39.5004","39.5005","39.5006","39.5007","39.5008","39.5009","39.5010","39.5011","39.5013","39.5014","39.5015","39.5016","39.5601","39.5602","39.5700x003","39.5701","39.5702","39.5900x001","39.5900x002","39.5900x003","39.5900x004","39.5900x005","39.5900x006","39.5900x007","39.5900x008","39.5900x009","39.5900x010","39.5900x011","39.5900x012","39.5900x013","39.5900x015","39.5900x016","39.5900x018","39.5900x019","39.5900x020","39.5900x021","39.5900x022","39.5900x023","39.5900x024","39.5900x025","39.5900x026","39.5900x027","39.5900x028","39.5900x029","39.5900x030","39.5900x031","39.7100x004","39.7101","39.7102","39.7103","39.7200x001","39.7200x004","39.7200x005","39.7209","39.7300x003","39.7300x004","39.7301","39.7302","39.7303","39.7400x002","39.7400x004","39.7800x001","39.7800x002","39.7900x007","39.7900x009","39.7900x010","39.7900x011","39.7900x013","39.7900x014","39.7900x015","39.7900x017","39.7900x019","39.7900x020","39.7900x021","39.7900x022","39.7900x023","39.7900x024","39.7900x025","39.7900x027","39.7902","39.7903","39.7904","39.7906","39.9000x010","39.9000x011","39.9000x012","39.9000x016","39.9000x017","39.9000x019","39.9000x020","39.9000x021","39.9000x022","39.9000x023","39.9000x024","39.9000x025","39.9000x026","39.9000x027","39.9000x028","39.9000x029","39.9000x030","39.9000x031","39.9000x032","39.9000x033","39.9000x034","39.9000x035","39.9000x036","39.9000x037","39.9001","39.9003","39.9004","39.9005","39.9006","39.9007","39.9008","39.9009","39.9010","39.9011","39.9012","39.9013","39.9015","39.9016","39.9100x003","39.9800x001","39.9801","40.2900x008","40.2904","40.2906","40.2908","40.2910","40.6100","40.6200","40.6300","40.6301","40.6400","40.6900x002","40.6900x003","40.6900x004","40.6901","40.9x00x003","40.9x00x004","40.9x00x005","40.9x00x006","40.9x00x007","40.9x00x008","40.9x00x009","40.9x00x010","40.9x00x011","40.9x00x012","40.9x00x013","40.9x00x014","40.9x00x015","40.9x00x016","40.9x00x017","40.9x01","40.9x02","40.9x03","40.9x04","40.9x05","40.9x06","40.9x07","40.9x08","40.9x09","41.2x01","41.2x02","41.2x03","41.4200x002","41.4200x003","41.4300","41.4301","41.5x00","41.5x01","41.9501","41.9502","41.9503","41.9504","42.0901","42.0902","42.1100","42.1200","42.1901","42.3310","42.4100","42.4100x009","42.4101","42.4102","42.4103","42.4104","42.4201","42.4202","42.4203","42.5100","42.5200","42.5200x005","42.5201","42.5202","42.5300x001","42.5500x001","42.5801","42.5802","42.5803","42.5900x001","42.6100","42.6200","42.6300","42.6400x002","42.6401","42.6402","42.6403","42.6500","42.6601","42.7x00x001","42.7x01","42.7x02","42.7x03","42.7x04","42.8100","42.8101","42.8200","42.8300","42.8400","42.8501","42.8502","43.0x00x003","43.0x02","43.0x03","43.1900x003","43.1900x005","43.5x00","43.5x00x003","43.5x00x007","43.5x01","43.5x02","43.5x03","43.6x00","43.6x00x005","43.6x00x006","43.6x01","43.6x02","43.7x00","43.7x00x001","43.7x01","43.7x02","43.7x03","43.8100","43.8201","43.8202","43.8901","43.8902","43.8903","43.9101","43.9102","43.9900x002","43.9900x003","43.9900x004","43.9901","43.9903","43.9905","44.4400x004","44.4400x005","44.4401","44.4403","44.5x00x002","44.5x00x004","44.5x00x005","44.5x01","44.5x02","44.5x03","44.5x04","44.5x05","44.5x06","44.5x07","44.6100x003","44.6200","44.6300x001","44.6301","44.6302","44.6400","44.6401","44.6500","44.6500x001","44.6500x002","44.6500x003","44.6501","44.6600x002","44.6601","44.6701","44.6800x002","44.6801","44.6902","44.9201","45.0100x005","45.0101","45.0102","45.0200x001","45.0201","45.0202","45.0203","45.0204","45.0300x002","45.0300x003","45.0301","45.0302","45.0303","45.1101","45.1200x001","45.6100","45.6200x001","45.6200x002","45.6201","45.6202","45.6203","45.6204","45.6205","45.6206","45.6207","45.6208","45.6300","45.7100x001","45.7200x002","45.7200x004","45.7201","45.7202","45.7203","45.7300x006","45.7300x007","45.7301","45.7302","45.7400x003","45.7401","45.7500","45.7501","45.7600x008","45.7600x018","45.7600x022","45.7601","45.7602","45.7603","45.7901","45.8100","45.8200","45.9100x006","45.9100x008","45.9103","45.9104","45.9200","45.9300x012","45.9300x013","45.9300x014","45.9300x015","45.9301","45.9302","45.9303","45.9304","45.9305","45.9306","45.9307","45.9310","45.9400x004","45.9400x009","45.9400x012","45.9400x016","45.9401","45.9402","45.9403","45.9404","45.9405","45.9406","45.9407","45.9408","45.9501","45.9502","45.9503","45.9504","46.0100x001","46.0101","46.0102","46.0300x001","46.0300x003","46.0300x004","46.0301","46.0302","46.0400x002","46.0401","46.0402","46.1000","46.1000x007","46.1100","46.1100x002","46.1300","46.1301","46.2100","46.2300x001","46.2301","46.2400","46.3200x002","46.3900x002","46.3900x006","46.3900x007","46.3901","46.3902","46.3904","46.3905","46.4101","46.4102","46.4103","46.4200","46.4201","46.4202","46.4300x004","46.4300x005","46.4301","46.4302","46.4303","46.5100x002","46.5100x004","46.5100x006","46.5101","46.5102","46.5200x006","46.5200x010","46.5200x011","46.5201","46.5202","46.5203","46.5204","46.7100","46.7200","46.7300x005","46.7301","46.7302","46.7303","46.7400x004","46.7401","46.7402","46.7403","46.7404","46.7405","46.7500x004","46.7501","46.7502","46.7503","46.7504","46.7505","46.7506","46.7601","46.7602","46.7603","46.7604","46.7900x009","46.7901","46.7902","46.7903","46.7904","46.8101","46.8102","46.8201","46.8202","46.9300x001","46.9301","46.9401","47.1100","47.1900x001","47.9200","48.0x00x002","48.0x00x003","48.0x01","48.0x02","48.0x03","48.1x00","48.2101","48.4900x002","48.4900x003","48.4901","48.4902","48.4903","48.4904","48.4905","48.5100","48.5100x002","48.5200","48.5201","48.5900x001","48.6100","48.6200","48.6201","48.6301","48.6302","48.6400x001","48.6500x001","48.6902","48.6903","48.6904","48.6905","48.7100","48.7101","48.7200","48.7300x001","48.7301","48.7302","48.7303","48.7400","48.7401","48.7501","48.7600x001","48.7600x002","48.7600x008","48.7601","48.7602","48.7603","48.7900x003","48.7901","48.9100","49.5901","49.7100","49.7200","49.7301","49.7302","49.7400x001","49.7501","49.7502","49.7600","49.7900x005","49.7901","49.7902","49.7903","49.7904","49.9901","50.0x00x004","50.0x00x008","50.0x00x016","50.0x01","50.0x02","50.2200","50.2200x003","50.2200x004","50.2200x005","50.2200x006","50.2200x007","50.2200x008","50.2200x009","50.2201","50.2202","50.2203","50.2204","50.2205","50.2206","50.3x01","50.3x02","50.3x03","50.3x04","50.3x05","50.3x06","50.4x00","50.6101","50.6900x002","50.6901","50.9900x003","51.2100","51.2200","51.2200x004","51.2201","51.3100","51.3201","51.3202","51.3203","51.3204","51.3400","51.3601","51.3602","51.3700x001","51.3700x002","51.3700x003","51.3700x007","51.3701","51.3702","51.3703","51.3704","51.3900x005","51.3900x008","51.3901","51.3902","51.3903","51.3904","51.3905","51.3906","51.3907","51.4201","51.4202","51.4301","51.4302","51.4303","51.4304","51.5100","51.5101","51.5900x005","51.5900x006","51.5900x008","51.5900x009","51.5901","51.5902","51.5903","51.5904","51.6100x001","51.7101","51.7200x001","51.7201","51.7202","51.7203","51.7204","51.7900x002","51.7900x005","51.7900x006","51.7901","51.7902","51.7903","51.7904","51.7906","51.8100","51.8101","51.8200x001","51.8200x002","51.8300x003","51.8301","51.9100","51.9101","51.9200","51.9300x001","51.9301","51.9302","51.9303","51.9304","51.9305","51.9401","51.9800x010","51.9901","52.1200","52.5100x001","52.5101","52.5102","52.5103","52.5104","52.5201","52.5202","52.5203","52.5204","52.5205","52.5206","52.5300","52.5301","52.5901","52.5902","52.5903","52.5904","52.5905","52.5906","52.6x00","52.6x00x003","52.6x01","52.7x00","52.7x00x003","52.7x01","52.9201","52.9500x001","52.9500x002","52.9501","52.9502","52.9503","52.9504","52.9601","52.9602","52.9603","52.9604","52.9605","53.7101","53.7201","53.7202","53.8000x001","53.8001","53.8100x001","53.8300x001","54.0x00x002","54.0x00x004","54.0x00x006","54.0x00x010","54.0x00x013","54.0x00x018","54.0x00x021","54.0x00x022","54.0x00x023","54.0x00x024","54.0x00x025","54.0x01","54.0x02","54.0x03","54.0x04","54.0x05","54.0x06","54.0x07","54.0x08","54.1100","54.1101","54.1201","54.1202","54.1900x001","54.1900x005","54.1900x006","54.1900x010","54.1900x011","54.1900x020","54.1900x023","54.1901","54.1902","54.1903","54.1904","54.1905","54.1906","54.1907","54.1909","54.2100","54.3x00x010","54.3x03","54.3x04","54.5100","54.5100x005","54.5100x009","54.5101","54.5103","54.5900x007","54.5901","54.5902","54.5903","54.5904","54.5906","54.6101","54.6301","54.6400","54.6401","54.7100","54.7200x001","54.7300x001","54.7301","54.7302","54.7400x001","54.7400x002","54.7400x003","54.7400x004","54.7400x005","54.7400x006","54.7401","54.7402","54.7403","54.7404","54.7405","54.7500x002","54.7501","54.7502","54.9201","54.9202","54.9300x001","54.9500x004","54.9501","54.9502","54.9801","54.9900x010","54.9900x017","55.0100x010","55.0101","55.0107","55.0109","55.0200","55.0201","55.0300x005","55.1100x001","55.1200","55.1200x001","55.5100","55.5101","55.5103","55.5104","55.5106","55.5200","55.5201","55.8101","55.8102","55.8602","55.8603","55.8605","55.8606","55.8701","55.8702","55.8703","55.8704","55.8901","56.4100","56.4105","56.4200","56.5101","56.5102","56.6100x001","56.6100x003","56.6100x004","56.7100x002","56.7101","56.7103","56.7200","56.7400","56.7402","56.7501","56.8200x002","56.8201","56.8500","56.8900x001","56.8900x006","56.8901","56.8907","56.8908","56.8909","57.1901","57.1903","57.1905","57.2100","57.7101","57.7102","57.7900x001","57.7901","57.8100","57.8500x002","57.8501","57.8900x001","57.9301","58.0x00x003","58.0x01","58.0x02","58.0x03","58.1x01","58.3903","58.3904","58.3906","58.4100","58.4600x001","58.4600x002","58.4600x003","58.4600x004","58.4600x005","58.4600x006","58.4600x007","58.4600x008","58.4601","58.4900x003","58.4901","59.0902","59.0903","59.1901","59.1902","60.9300","61.4102","61.4202","61.4902","61.4904","62.4100x004","62.4101","62.6100","62.6900x001","63.5101","63.5200x001","63.5201","63.5202","63.5203","63.5900","63.8101","63.8102","64.4100","64.4500x002","64.4904","64.4905","65.7300x001","65.7400","65.7500","65.7600","65.7900x008","65.7900x009","65.7901","65.7902","65.7903","65.7904","65.7905","65.8102","65.8900x001","65.8901","65.8902","66.7100","66.7901","66.7902","66.7904","66.7905","67.6100","68.0x00x004","68.0x00x005","68.4901","69.2300","69.2901","69.4100","69.4200","69.4900x005","69.4900x006","69.4903","70.1300","70.5305","70.6200x001","70.6200x002","70.7200","70.7300","70.7400x001","70.7401","70.7900x005","70.7900x006","70.7900x010","70.7901","70.7902","70.7903","70.7905","70.7906","70.7907","70.7909","71.7101","71.7102","71.7900x008","71.7900x010","71.7900x011","71.7900x012","71.7900x013","71.7901","71.7903","85.1200x001","85.2100x003","85.2100x019","85.2100x020","85.2101","85.2200","85.2300x001","85.2301","85.2401","85.2402","85.2500","85.3300x001","85.3401","85.3500x001","85.3600x001","85.3601","85.4100x001","85.4200x001","85.8100","85.8601","85.8700x003","85.8701","85.8702","85.8900x005","85.8900x007","85.8900x008","85.9100","86.2300x001","86.2300x002","86.2300x003","86.2300x005","86.2301","86.2400x001","86.4x01","86.4x02","86.4x03","86.5900x006","86.8100x002","86.8600x001","86.8701","86.8702","86.8900x002","86.8900x010","86.8900x011","86.8900x014","86.8901","86.8902","98.1800x001","98.1900x001","98.2600x001","98.2700x001","98.2800x001","98.2900x001"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合VJ1入组条件，匹配规则：某一手术匹配')
    
    if MDCV_DRG.VJ11_group(record):
      return 'VJ11'

    if MDCV_DRG.VJ13_group(record):
      return 'VJ13'

    if MDCV_DRG.VJ15_group(record):
      return 'VJ15'

    return 'VJ1'
  else:
    return ''

