from python_enigma import enigma

use_these = [("I", "D"), ("II", "O"), ("III", "O")]
machine = enigma.Enigma(catalog="default", stecker="IS FW LB AO GR EJ XK CT DU MV",
                        rotors=use_these, reflector="Reflector B", operator=True, word_length=5, stator="military")
machine.set_wheels("EFC")

crypted = 'ZPZUM KGTOD RADRP DROCC ALCFD ZUVIJ CPYND JDSVR LCJEE FUKRE LZJKW QCPDM CXPRP QMDTK KCMEY XS'
print(crypted)
print("If I feed that back through, it decrypts to:")
machine.set_wheels("EFC")
print(machine.parse(crypted))
exit()