import discord
import datetime
import os
import openpyxl


client=discord.Client()

access_token=os.environ["BOT_TOKEN"]



@client.event
async def on_ready():
    print(client.user.name)
    print('started bot')    
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="정답 받는중"))

@client.event
async def on_message(message):
    if message.content.startswith("!"):
        if message.content == "!시간표":
            today=datetime.datetime.today().weekday()
            if today==0:
                emb=discord.Embed(color=0xff9900)
                emb.add_field(name="오늘의 시간표",value="월요일",inline=False)
                emb.add_field(name="조회",value="https://zoom.us/j/4620065666?pwd=aDJ1T2ZSQkRaSVFBaEczSmtMVk9CZz09#success")
                emb.add_field(name="1교시", value="[국어](https://zoom.us/postattendee?mn=6kqirr5rS6FQCgP-gtJl3jduQqU_Ct6epa8.XWHsVVFJcTf2V4OP&id=2)", inline=False)           
                emb.add_field(name="2교시", value="[영어](https://zoom.us/j/6924056614?pwd=WGR1SGsrU0xhVlFXcWFKbjlmcExxUT09#success)", inline=False)
                emb.add_field(name="3교시", value="[음악](https://zoom.us/j/8992587200?pwd=WnRDY0ZLUUJPdTE0VWMrVTdCUHlQQT09#success)",inline=False)
                emb.add_field(name="4교시", value="[도덕](https://us02web.zoom.us/j/6725551179?pwd=QjBsYWh4cGlVRUNtcnJyeGxQNEpYZz09#success)",inline=False)
                emb.add_field(name="5교시", value="[역사](https://zoom.us/j/6404846050?pwd=MklheVFUOUlnclVFd1l5OXlxRnBTUT09#success)",inline=False)
                emb.add_field(name="6교시", value="[과학](https://zoom.us/j/3440254414?pwd=alNVQ0NlS0VYdkZoRWlLeWhpS2thQT09#success)",inline=False)
                await message.channel.send(embed=emb)
            elif today==1:
                emb=discord.Embed(color=0xff9900)
                emb.add_field(name="오늘의 시간표",value="화요일",inline=False)
                emb.add_field(name="조회",value="https://zoom.us/j/4620065666?pwd=aDJ1T2ZSQkRaSVFBaEczSmtMVk9CZz09#success")
                emb.add_field(name="1교시", value="[과학](https://zoom.us/j/3440254414?pwd=alNVQ0NlS0VYdkZoRWlLeWhpS2thQT09#success)", inline=False)
                emb.add_field(name="2교시", value="[수학](https://us02web.zoom.us/j/6718992309?pwd=ci8rQVByUXVPMElwQ01ITlBwUmxLdz09#success)", inline=False)
                emb.add_field(name="3교시", value="[국어](https://zoom.us/postattendee?mn=6kqirr5rS6FQCgP-gtJl3jduQqU_Ct6epa8.XWHsVVFJcTf2V4OP&id=2)",inline=False)           
                emb.add_field(name="4교시", value="[역사](https://zoom.us/j/6404846050?pwd=MklheVFUOUlnclVFd1l5OXlxRnBTUT09#success)",inline=False)
                emb.add_field(name="5교시", value="[미술](https://zoom.us/j/2210779923?pwd=MHlPMjJkYnV2QmhZRVdRZWk1bnBxdz09#success)",inline=False)
                emb.add_field(name="6교시", value="[한문](https://zoom.us/j/4620065666?pwd=aDJ1T2ZSQkRaSVFBaEczSmtMVk9CZz09#success)",inline=False)
                emb.add_field(name="7교시", value="[영어](https://zoom.us/j/6924056614?pwd=WGR1SGsrU0xhVlFXcWFKbjlmcExxUT09#success)",inline=False)
                await message.channel.send(embed=emb)
            elif today==2:
                emb=discord.Embed(color=0xff9900)
                emb.add_field(name="오늘의 시간표",value="수요일",inline=False)
                emb.add_field(name="조회",value="https://zoom.us/j/4620065666?pwd=aDJ1T2ZSQkRaSVFBaEczSmtMVk9CZz09#success")
                emb.add_field(name="1교시", value="[영어](https://zoom.us/j/6924056614?pwd=WGR1SGsrU0xhVlFXcWFKbjlmcExxUT09#success)", inline=False)
                emb.add_field(name="2교시", value="[체육](https://www.ebsoc.co.kr/)", inline=False)
                emb.add_field(name="3교시", value="[미술](https://zoom.us/j/2210779923?pwd=MHlPMjJkYnV2QmhZRVdRZWk1bnBxdz09#success)",inline=False)
                emb.add_field(name="4교시", value="[수학](https://us02web.zoom.us/j/6718992309?pwd=ci8rQVByUXVPMElwQ01ITlBwUmxLdz09#success)",inline=False)
                emb.add_field(name="5교시", value="[도덕](https://us02web.zoom.us/j/6725551179?pwd=QjBsYWh4cGlVRUNtcnJyeGxQNEpYZz09#success)",inline=False)
                emb.add_field(name="6교시", value="스포츠",inline=False)
                await message.channel.send(embed=emb)
            elif today==3:
                emb=discord.Embed(color=0xff9900)
                emb.add_field(name="오늘의 시간표",value="목요일",inline=False)
                emb.add_field(name="조회",value="https://zoom.us/j/4620065666?pwd=aDJ1T2ZSQkRaSVFBaEczSmtMVk9CZz09#success")
                emb.add_field(name="1교시", value="[국어](https://zoom.us/postattendee?mn=6kqirr5rS6FQCgP-gtJl3jduQqU_Ct6epa8.XWHsVVFJcTf2V4OP&id=2)", inline=False)            
                emb.add_field(name="2교시", value="[영어](https://zoom.us/j/6924056614?pwd=WGR1SGsrU0xhVlFXcWFKbjlmcExxUT09#success)", inline=False)
                emb.add_field(name="3교시", value="[수학](https://us02web.zoom.us/j/6718992309?pwd=ci8rQVByUXVPMElwQ01ITlBwUmxLdz09#success)",inline=False)
                emb.add_field(name="4교시", value="[체육](https://www.ebsoc.co.kr/)",inline=False)
                emb.add_field(name="5교시", value="[자율](https://zoom.us/j/4620065666?pwd=aDJ1T2ZSQkRaSVFBaEczSmtMVk9CZz09#success)",inline=False)
                emb.add_field(name="6교시", value="[과학](https://zoom.us/j/3440254414?pwd=alNVQ0NlS0VYdkZoRWlLeWhpS2thQT09#success)",inline=False)
                emb.add_field(name="7교시", value="[정보](https://zoom.us/j/7525745591?pwd=YjlRQ1JWNDFxM1lsUUdmNEZraHhLZz09#success)",inline=False)
                await message.channel.send(embed=emb)
            elif today==4:
                emb=discord.Embed(color=0xff9900)
                emb.add_field(name="오늘의 시간표",value="금요일",inline=False)
                emb.add_field(name="조회",value="https://zoom.us/j/4620065666?pwd=aDJ1T2ZSQkRaSVFBaEczSmtMVk9CZz09#success")
                emb.add_field(name="1교시", value="[체육](https://www.ebsoc.co.kr/)", inline=False)
                emb.add_field(name="2교시", value="[국어](https://zoom.us/postattendee?mn=6kqirr5rS6FQCgP-gtJl3jduQqU_Ct6epa8.XWHsVVFJcTf2V4OP&id=2)", inline=False)            
                emb.add_field(name="3교시", value="[한문](https://zoom.us/j/4620065666?pwd=aDJ1T2ZSQkRaSVFBaEczSmtMVk9CZz09#success)",inline=False)
                emb.add_field(name="4교시", value="[수학](https://us02web.zoom.us/j/6718992309?pwd=ci8rQVByUXVPMElwQ01ITlBwUmxLdz09#success)",inline=False)
                emb.add_field(name="5교시", value="[과학](https://zoom.us/j/3440254414?pwd=alNVQ0NlS0VYdkZoRWlLeWhpS2thQT09#success)",inline=False)
                emb.add_field(name="6교시", value="[역사](https://zoom.us/j/6404846050?pwd=MklheVFUOUlnclVFd1l5OXlxRnBTUT09#success)",inline=False)
                await message.channel.send(embed=emb)
            else:
                await message.channel.send("오늘은 등교일이 아닙니다")

        if message.content=="!도움":
            em=discord.Embed(color=0xff9900)
            em.add_field(name="!시간표",value="오늘의 시간표를 보여주는 명령입니다.(수업 접속링크도 함께)",inline=False)
            em.add_field(name="!퀴즈",value="이번주 퀴즈 내용을 보여주는 명령어 입니다.",inline=False)
            em.add_field(name="!정답: OOO",value="이번주 퀴즈의 정답을 입력하는 명령어 입니다.(ex> !정답: 홍길동)",inline=False)
            em.add_field(name="!정답보기", value="이번주 퀴즈의 정답자와 답을 보여주는 명령어 입니다.", inline=False)
            em.add_field(name="!급식",value="오늘의 급식을 안내하는 명령어 입니다.",inline=False)
            em.add_field(name="!내정보",value="자신이 맞춘 퀴즈개수와 레벨등을 안내하는 명령어 입니다.",inline=False)
            em.add_field(name="!배워",value="단어를 학습시키는 명령어 입니다.(!배워 학습시킬단어 단어뜻)",inline=False)
            em.add_field(name="!알려줘",value="학습시킨 단어를 불러오는 명령어 입니다.(!알려줘 학습시킨 단어)")
            await message.channel.send(embed=em)
        
        if message.content=="!급식":
            await message.channel.send("업데이트 예정")

        if message.content=="!퀴즈":
            await message.channel.send("업데이트 예정")

        if message.content == "!정답: 000":
            await message.channel.send("정답입니다.")

        elif message.content.startswith("!정답:"):
            await message.channel.send("오답입니다.") 

        if message.content== "!정답보기":
            await message.channel.send("업데이트 예정")

        if message.content.startswith("!배워"):
            file=openpyxl.load_workbook("discord_bot1.xlsx")
            sheet=file.active
            learn=message.content.split(" ")
            for i in range(1,101):
                if sheet["A"+str(i)].value=="-":
                    sheet["A"+str(i)].value = learn[1]
                    sheet["B"+str(i)].value = learn[2]
                    await message.channel.send("단어가 학습되었습니다.")
                    break
                file.save("discord_bot1.xlsx")

        if message.content.startswith("!알려줘"):
            file=openpyxl.load_workbook("discord_bot1.xlsx")
            sheet=file.active
            remem=message.content.split(" ")
            for i in range(1,101):
                if sheet["A"+str(i)].value==remem[1]:
                    await client.send_message(message.channel, sheet["B"+str(i)].value)
                    break
            
        else:
            await message.channel.send("도움이 필요하신가요?")


client.run(access_token)
