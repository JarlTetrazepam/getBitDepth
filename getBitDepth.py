import os
import soundfile as sf

# CWD as target
directory = os.fsencode(os.getcwd())
    
greaterThan24 = []
for file in os.listdir(directory):
    filename = os.fsdecode(file)

    try:
        ob = sf.SoundFile(filename)
        bitDepth = format(ob.subtype)[-2:]
        if not format(ob.subtype)[:3] == "PCM":
            #print(format(ob.subtype) + " " + filename)
            greaterThan24.append(filename)
        else:
            if int(bitDepth) > 24:
                greaterThan24.append(filename)
    
    except sf.LibsndfileError:
        continue
    except Exception as error:
        print(error)
if len(greaterThan24) > 0:
    print("The follwing files might have a bit depth greater than 24:\n")

    for filename in greaterThan24:
        print(filename)

else: 
    print("All files most likely have a bit depth of 24 or below")

# Note that mp3 files show a sf.subtype of float as well, and I am unsure what their bit depth is. It shouldn't matter however, as those aren't to be played on a cdj setup anyway