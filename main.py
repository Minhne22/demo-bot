from telethon import TelegramClient
from telethon import events
from telethon.tl.custom.message import Message

client = TelegramClient('MinhBet', 20444528, '40308089a273f061bb07a23a96f2c8e7')
client.start()

tien_cuoc = int(input("Tiền cược: "))
tien_lo = int(input("Tiền lỗ: "))
tien_lai = int(input("Tiền lãi: "))

trang_thai = 0

print("""
Mode 1: Đặt theo bên nhiều
Mode 2: Đặt theo bên ít
""")
while True:
    mode = input("Chọn mode: ")
    if mode in ["1", "2"]:
        break
    print("Chỉ nhập 1 hoặc 2")

dat = ''



@client.on(events.NewMessage(chats='@laucuataixiuroom'))
async def handler(event: Message):
    global dat
    if event.from_id.user_id == 6422312899:
        text = event.text
        # print(text)
        if 'Còn 9s để đặt cược' in text:
            print("Đặt")
            tien_tai = text.split('Cửa Tài:')[1].split('Tổng tiền ')[1].split('\xa0₫')[0]
            tien_xiu = text.split('Cửa Xỉu:')[1].split('Tổng tiền ')[1].split('\xa0₫')[0]
            # print(tien_tai, tien_xiu)
            if tien_tai == tien_xiu:
                return
            dat = "TAI"
            if (float(tien_tai) < float(tien_xiu) and mode == "1") or (float(tien_tai) > float(tien_xiu) and mode == "2"):
                    dat = "XIU"
            await event.respond(f'{dat[0]} {tien_cuoc}')
        
        elif 'Kết quả cược phiên: ' in text:
            ketqua = text.split('Cửa thắng : ')[1].split('\n')[0].strip()
            if dat:
                if ketqua == dat:
                    trang_thai += tien_cuoc
                else:
                    trang_thai -= tien_cuoc
                print(f'Tiền dư hiện tại: {trang_thai}')
                
                if trang_thai >= tien_lai:
                    print('Chốt lãi')
                    await client.disconnect()
                elif (trang_thai * -1) >= tien_lo:
                    print('Chốt lỗ')
                    await client.disconnect()
                    
            
                    
                
            

# Chạy bot
client.run_until_disconnected()


