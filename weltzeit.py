from datetime import datetime, timedelta


def world_times():
    meine_stadt = datetime.now()
    lissabon = meine_stadt + timedelta(hours=-1)
    washington = meine_stadt + timedelta(hours=-5)
    losangeles = meine_stadt + timedelta(hours=-8)
    hawaii = meine_stadt + timedelta(hours=-10)
    moskau = meine_stadt + timedelta(hours=+3)
    bangkok = meine_stadt + timedelta(hours=+7)
    tokio = meine_stadt + timedelta(hours=+9)

    all_times = f'''Es ist {meine_stadt:%H:%M} Uhr in meiner Stadt. 
 Das bedeutet, in Lissabon ist es {lissabon:%H:%M} Uhr.
 Das bedeutet, in Washington D.C. ist es {washington:%H:%M} Uhr.
 Das bedeutet, in Los Angeles ist es {losangeles:%H:%M} Uhr.
 Das bedeutet, in Hawaii ist es {hawaii:%H:%M} Uhr.
 Das bedeutet, in Moskau ist es {moskau:%H:%M} Uhr.
 Das bedeutet, in Bangkok ist es {bangkok:%H:%M} Uhr.
 Das bedeutet, in Tokio ist es {tokio:%H:%M} Uhr.'''

    print('\n', all_times)


world_times()
