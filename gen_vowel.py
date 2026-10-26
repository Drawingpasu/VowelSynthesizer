from VowelSynthesizer import generator, dBFilter
import numpy as np

def make_sound(vowel, f0, duration1, sample_rate = 48000): #vowel은 char, f0은 튜플, duration은 float
    if vowel == 'ㅏ' or vowel == '아':
        f0 = list(f0)
        f0[0] = int(f0[0])
        f0[1] = int(f0[1])

        #배음 몇개 만들어야 할지 계산
        min = f0[0] if f0[0] < f0[1] else f0[1]
        count = round(1560/min) # round(a / min)의 a에는 그 모음 배음의 최대 주파수를 적음 ('아'는 5배음이 끝이라 1560)


        #배음 생성
        output = generator.generate_sin(duration = duration1, freqL=0, freqR=0, dB=-100, sample_rate=sample_rate)
        for i in range(1, count + 1):
            curfreq = i * f0[0]
            nextfreq = i * f0[1]

            #dBFilter에서 주파수 dB 필터 가져와서
            if f0[0] <= f0[1]: #음 상승할때 or 일정할때
                filternp = dBFilter.dBfilterA()[curfreq-1 : nextfreq]
            else: #음 내려갈때
                filternp = dBFilter.dBfilterA()[nextfreq-1 : curfreq]
                filternp = np.flip(filternp)

            #맞게 보간한 다음에
            x = np.linspace(0, 1, abs(curfreq - nextfreq) + 1)
            y = filternp
            new_filter = np.interp(np.linspace(0, 1, int(sample_rate*duration1)), x, y)

            # 페이드 인 페이드 아웃
            a = np.linspace(-30, 0, 500)
            ac = np.zeros(int(sample_rate * duration1) - 500)
            fadein = np.append(a, ac)
            b = np.linspace(0, -30, 500)
            bc = np.zeros(int(sample_rate * duration1) - 500)
            fadeout = np.append(bc, b)

            # 씌우기
            audio = generator.generate_sin(duration = duration1, freqL=curfreq, freqR=nextfreq, dB=new_filter+fadein+fadeout, sample_rate=sample_rate)
            output = output + audio


        return output



    elif vowel == 'ㅐ' or vowel == '애' or vowel == 'ㅔ' or vowel == '에':
        f0 = list(f0)
        f0[0] = int(f0[0])
        f0[1] = int(f0[1])
    
        #배음 몇개 만들어야 할지 계산
        min = f0[0] if f0[0] < f0[1] else f0[1]
        count = round(2600/min) # round(a / min)의 a에는 그 모음 배음의 최대 주파수를 적음 ('아'는 5배음이 끝이라 1560)


        #배음 생성
        output = generator.generate_sin(duration = duration1, freqL=0, freqR=0, dB=-100, sample_rate=sample_rate)
        for i in range(1, count + 1):
            curfreq = i * f0[0]
            nextfreq = i * f0[1]
    
            #dBFilter에서 주파수 dB 필터 가져와서
            if f0[0] <= f0[1]: #음 상승할때 or 일정할때
                 filternp = dBFilter.dBfilterE()[curfreq-1 : nextfreq]
            else: #음 내려갈때
                 filternp = dBFilter.dBfilterE()[nextfreq-1 : curfreq]
                 filternp = np.flip(filternp)
        
             #맞게 보간한 다음에
            x = np.linspace(0, 1, abs(curfreq - nextfreq) + 1)
            y = filternp
            new_filter = np.interp(np.linspace(0, 1, int(sample_rate*duration1)), x, y)
    
            # 페이드 인 페이드 아웃
            a = np.linspace(-30, 0, 500)
            ac = np.zeros(int(sample_rate * duration1) - 500)
            fadein = np.append(a, ac)
            b = np.linspace(0, -30, 500)
            bc = np.zeros(int(sample_rate * duration1) - 500)
            fadeout = np.append(bc, b)

            # 씌우기
            audio = generator.generate_sin(duration = duration1, freqL=curfreq, freqR=nextfreq, dB=new_filter+fadein+fadeout, sample_rate=sample_rate)
            output = output + audio
        
        
        return output



    elif vowel == 'ㅣ' or vowel == '이':
        f0 = list(f0)
        f0[0] = int(f0[0])
        f0[1] = int(f0[1])
        
        #배음 몇개 만들어야 할지 계산
        min = f0[0] if f0[0] < f0[1] else f0[1]
        count = round(2340/min) # round(a / min)의 a에는 그 모음 배음의 최대 주파수를 적음 ('아'는 5배음이 끝이라 1560)
    
    
        #배음 생성
        output = generator.generate_sin(duration = duration1, freqL=0, freqR=0, dB=-100, sample_rate=sample_rate)
        for i in range(1, count + 1):
            curfreq = i * f0[0]
            nextfreq = i * f0[1]
        
            #dBFilter에서 주파수 dB 필터 가져와서
            if f0[0] <= f0[1]: #음 상승할때 or 일정할때
                 filternp = dBFilter.dBfilterI()[curfreq-1 : nextfreq]
            else: #음 내려갈때
                 filternp = dBFilter.dBfilterI()[nextfreq-1 : curfreq]
                 filternp = np.flip(filternp)
        
             #맞게 보간한 다음에
            x = np.linspace(0, 1, abs(curfreq - nextfreq) + 1)
            y = filternp
            new_filter = np.interp(np.linspace(0, 1, int(sample_rate*duration1)), x, y)
    
            # 페이드 인 페이드 아웃
            a = np.linspace(-30, 0, 500)
            ac = np.zeros(int(sample_rate * duration1) - 500)
            fadein = np.append(a, ac)
            b = np.linspace(0, -30, 500)
            bc = np.zeros(int(sample_rate * duration1) - 500)
            fadeout = np.append(bc, b)

            # 씌우기
            audio = generator.generate_sin(duration = duration1, freqL=curfreq, freqR=nextfreq, dB=new_filter+fadein+fadeout, sample_rate=sample_rate)
            output = output + audio
        
        
        return output


    elif vowel == 'ㅗ' or vowel == '오':
            f0 = list(f0)
            f0[0] = int(f0[0])
            f0[1] = int(f0[1])
        
            #배음 몇개 만들어야 할지 계산
            min = f0[0] if f0[0] < f0[1] else f0[1]
            count = round(1300/min) # round(a / min)의 a에는 그 모음 배음의 최대 주파수를 적음 ('아'는 5배음이 끝이라 1560)
    
    
            #배음 생성
            output = generator.generate_sin(duration = duration1, freqL=0, freqR=0, dB=-100, sample_rate=sample_rate)
            for i in range(1, count + 1):
                curfreq = i * f0[0]
                nextfreq = i * f0[1]
        
                #dBFilter에서 주파수 dB 필터 가져와서
                if f0[0] <= f0[1]: #음 상승할때 or 일정할때
                     filternp = dBFilter.dBfilterO()[curfreq-1 : nextfreq]
                else: #음 내려갈때
                     filternp = dBFilter.dBfilterO()[nextfreq-1 : curfreq]
                     filternp = np.flip(filternp)
            
                 #맞게 보간한 다음에
                x = np.linspace(0, 1, abs(curfreq - nextfreq) + 1)
                y = filternp
                new_filter = np.interp(np.linspace(0, 1, int(sample_rate*duration1)), x, y)
        
                # 페이드 인 페이드 아웃
                a = np.linspace(-30, 0, 500)
                ac = np.zeros(int(sample_rate * duration1) - 500)
                fadein = np.append(a, ac)
                b = np.linspace(0, -30, 500)
                bc = np.zeros(int(sample_rate * duration1) - 500)
                fadeout = np.append(bc, b)
    
                # 씌우기
                audio = generator.generate_sin(duration = duration1, freqL=curfreq, freqR=nextfreq, dB=new_filter+fadein+fadeout, sample_rate=sample_rate)
                output = output + audio
            
            
            return output
    
    
    
    elif vowel == 'ㅜ' or vowel == '우':
        f0 = list(f0)
        f0[0] = int(f0[0])
        f0[1] = int(f0[1])
        
        #배음 몇개 만들어야 할지 계산
        min = f0[0] if f0[0] < f0[1] else f0[1]
        count = round(1300/min) # round(a / min)의 a에는 그 모음 배음의 최대 주파수를 적음 ('아'는 5배음이 끝이라 1560)
    
    
        #배음 생성
        output = generator.generate_sin(duration = duration1, freqL=0, freqR=0, dB=-100, sample_rate=sample_rate)
        for i in range(1, count + 1):
            curfreq = i * f0[0]
            nextfreq = i * f0[1]
        
            #dBFilter에서 주파수 dB 필터 가져와서
            if f0[0] <= f0[1]: #음 상승할때 or 일정할때
                 filternp = dBFilter.dBfilterU()[curfreq-1 : nextfreq]
            else: #음 내려갈때
                 filternp = dBFilter.dBfilterU()[nextfreq-1 : curfreq]
                 filternp = np.flip(filternp)
        
             #맞게 보간한 다음에
            x = np.linspace(0, 1, abs(curfreq - nextfreq) + 1)
            y = filternp
            new_filter = np.interp(np.linspace(0, 1, int(sample_rate*duration1)), x, y)
    
            # 페이드 인 페이드 아웃
            a = np.linspace(-30, 0, 500)
            ac = np.zeros(int(sample_rate * duration1) - 500)
            fadein = np.append(a, ac)
            b = np.linspace(0, -30, 500)
            bc = np.zeros(int(sample_rate * duration1) - 500)
            fadeout = np.append(bc, b)

            # 씌우기
            audio = generator.generate_sin(duration = duration1, freqL=curfreq, freqR=nextfreq, dB=new_filter+fadein+fadeout, sample_rate=sample_rate)
            output = output + audio
        
        
        return output


    elif vowel == 'ㅡ' or vowel == '으':
            f0 = list(f0)
            f0[0] = int(f0[0])
            f0[1] = int(f0[1])
        
            #배음 몇개 만들어야 할지 계산
            min = f0[0] if f0[0] < f0[1] else f0[1]
            count = round(1560/min) # round(a / min)의 a에는 그 모음 배음의 최대 주파수를 적음 ('아'는 5배음이 끝이라 1560)
    
    
            #배음 생성
            output = generator.generate_sin(duration = duration1, freqL=0, freqR=0, dB=-100, sample_rate=sample_rate)
            for i in range(1, count + 1):
                curfreq = i * f0[0]
                nextfreq = i * f0[1]
        
                #dBFilter에서 주파수 dB 필터 가져와서
                if f0[0] <= f0[1]: #음 상승할때 or 일정할때
                     filternp = dBFilter.dBfilterEU()[curfreq-1 : nextfreq]
                else: #음 내려갈때
                     filternp = dBFilter.dBfilterEU()[nextfreq-1 : curfreq]
                     filternp = np.flip(filternp)
            
                 #맞게 보간한 다음에
                x = np.linspace(0, 1, abs(curfreq - nextfreq) + 1)
                y = filternp
                new_filter = np.interp(np.linspace(0, 1, int(sample_rate*duration1)), x, y)
        
                # 페이드 인 페이드 아웃
                a = np.linspace(-30, 0, 500)
                ac = np.zeros(int(sample_rate * duration1) - 500)
                fadein = np.append(a, ac)
                b = np.linspace(0, -30, 500)
                bc = np.zeros(int(sample_rate * duration1) - 500)
                fadeout = np.append(bc, b)
    
                # 씌우기
                audio = generator.generate_sin(duration = duration1, freqL=curfreq, freqR=nextfreq, dB=new_filter+fadein+fadeout, sample_rate=sample_rate)
                output = output + audio
            
            
            return output
    
    
    
    elif vowel == 'ㅓ' or vowel == '어':
        f0 = list(f0)
        f0[0] = int(f0[0])
        f0[1] = int(f0[1])
            
         #배음 몇개 만들어야 할지 계산
        min = f0[0] if f0[0] < f0[1] else f0[1]
        count = round(1300/min) # round(a / min)의 a에는 그 모음 배음의 최대 주파수를 적음 ('아'는 5배음이 끝이라 1560)
    
    
        #배음 생성
        output = generator.generate_sin(duration = duration1, freqL=0, freqR=0, dB=-100, sample_rate=sample_rate)
        for i in range(1, count + 1):
            curfreq = i * f0[0]
            nextfreq = i * f0[1]
        
            #dBFilter에서 주파수 dB 필터 가져와서
            if f0[0] <= f0[1]: #음 상승할때 or 일정할때
                 filternp = dBFilter.dBfilterEO()[curfreq-1 : nextfreq]
            else: #음 내려갈때
                 filternp = dBFilter.dBfilterEO()[nextfreq-1 : curfreq]
                 filternp = np.flip(filternp)
        
             #맞게 보간한 다음에
            x = np.linspace(0, 1, abs(curfreq - nextfreq) + 1)
            y = filternp
            new_filter = np.interp(np.linspace(0, 1, int(sample_rate*duration1)), x, y)
    
            # 페이드 인 페이드 아웃
            a = np.linspace(-30, 0, 500)
            ac = np.zeros(int(sample_rate * duration1) - 500)
            fadein = np.append(a, ac)
            b = np.linspace(0, -30, 500)
            bc = np.zeros(int(sample_rate * duration1) - 500)
            fadeout = np.append(bc, b)

            # 씌우기
            audio = generator.generate_sin(duration = duration1, freqL=curfreq, freqR=nextfreq, dB=new_filter+fadein+fadeout, sample_rate=sample_rate)
            output = output + audio
        
        
        return output

    return None
