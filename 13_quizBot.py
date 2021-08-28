import asyncio
import discord
import datetime
import os
import openpyxl


client=discord.Client()

access_token=os.environ["BOT_TOKEN"]

yes = "⭕"
no = "❌"
reactions = [yes, no]

@client.event
async def on_ready():
    print(client.user.name)
    print('started bot')    
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name="정답 받는중"))

@client.event
async def on_message(message):
    def check(reaction, user):
        return user == message.author and str(reaction.emoji) in reactions

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

        elif message.content=="!도움":
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
        
        elif message.content=="!급식":
            await message.channel.send("업데이트 예정")

        elif message.content=="!퀴즈":
            await message.channel.send("업데이트 예정")

        elif message.content == "!정답: 000":
            await message.channel.send("정답입니다.")

        elif message.content.startswith("!정답:"):
            await message.channel.send("오답입니다.") 

        elif message.content== "!정답보기":
            await message.channel.send("업데이트 예정")

        elif message.content.startswith("!배워"):
            await message.channel.send("업데이트 예정")            

        elif message.content.startswith("!알려줘"):
            await message.channel.send("업데이트 예정")
            
        elif message.content == "!가입":
            file = openpyxl.load_workbook("memberlist.xlsx")
            wb = file.active
            for i in range(1, 101):
                if wb["A" + str(i)].value == str(message.author.id):
                    await message.channel.send("이미 가입된 사용자입니다.")
                    break

                elif wb["A" + str(i)].value == None:
                    embed = discord.Embed(title="회원 가입을 진행합니다", description="아래의 이모지에 반응하세요.")
                    msg = await message.channel.send(embed=embed)
                    await msg.add_reaction(yes)
                    await msg.add_reaction(no)

                    try:
                        reaction, user=await client.wait_for("reaction_add", check=check, timeout=15)
                    
                        if str(reaction.emoji) == yes:
                            await msg.delete()                

                            wb["A" + str(i)].value = str(message.author.id)
                            wb["B" + str(i)].value = str(message.author)
                            wb["C" + str(i)].value = str(datetime.datetime.now().replace(microsecond=0))
                            await message.channel.send("가입이 완료되었습니다.")
                            break
            
                        elif str(reaction.emoji) == no:
                            await msg.delete()
                            await message.channel.send("취소 되었습니다.")
                            break
                        
                    except asyncio.exceptions.TimeoutError:
                        await msg.delete()
                        await message.channel.send("시간이 초과되었습니다")

            file.save("memberlist.xlsx")




client.run(access_token)
