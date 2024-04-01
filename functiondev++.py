# def uzunlikni_top():
#     l = int(input("Santemetr kirit "))
#     m = l/100
#     return m 
# print(uzunlikni_top())

#2.
# def tonnalrda_top():
#     m = float(input("Kilogramm kirit "))
#     t = m/1000
#     return t 
# print(tonnalrda_top())

#3.
# def kilobaytlarda_top():
#     РОМА = float(input("Fayilning hajmini kirit "))
#     РОМА/1024
#     return РОМА
# print(kilobaytlarda_top())

# 4.
# def a_va_b_kesma_qancha():
#     a = float(input("A kesmani kirit "))
#     b = float(input("B kesmani kirit "))
#     ab = a/b
#     return ab
# print(a_va_b_kesma_qancha())

# 5.
# def a_va_b_kesma_qancha():
#     a = float(input("A kesmani kirit "))
#     b = float(input("B kesmani kirit "))
#     ab = a%b
#     return ab
# print(a_va_b_kesma_qancha())

# # 6.
# def onliklar_oxirgi_sonni_top(son):
#     a = son % 10
#     return a

# 7.
# def birliklar_oxirigi_sonini_top(son):
#     b = son // 10
#     return b 

# def final():
#     son = int(input("Ikki xonali son kirit "))

#     if son>99:
#         print("Faqat ikki xonali son kiriting")
#     else:
#         a = onliklar_oxirgi_sonni_top(son)
#         b = birliklar_oxirigi_sonini_top(son)

#         print(f"O'nliklar xonasidagi raqam: {a}")
#         print(f"Birlar xonasidagi raqam: {b}")
# final()


# def onliklar_oxirgi_sonni_top(son):
#     a = son % 10
#     return a 

# def birliklar_oxirigi_sonini_top(son):
#     b = son // 10
#     return b 

# def a_va_b_raqamlar_yigindisi():
#     son = int(input("Son kirit "))
#     if son > 100:
#         print("Faqat ikki xonali son kiriting")
#     else:
#         a = onliklar_oxirgi_sonni_top(son)
#         b = birliklar_oxirigi_sonini_top(son)
#         # print(f"O'nliklar xonasidagi raqam: {a} Birlar xonasidagi raqam: {b}")
#         print(a+b)
# a_va_b_raqamlar_yigindisi()


# 8.
# def almashtirish():
#     birlik = son % 10
#     unlik = son // 10
#     yangi_son = birlik * 10 + unlik
#     return yangi_son
# son = int(input("Ikki xonali son kiriting: "))
# if son > 100:
#     print("Faqat ikki xonali son kiriting ")
# else:
#     yangi_son = almashtirish()
#     print(yangi_son)


# 9.
# def yuzlar_xonasini_aniklovchi(son):
#     yuzlar_xonasi = (son // 100) % 10
#     return yuzlar_xonasi
# uchxonali_son = int(input("Uchxonali son kiriting: "))
# yuzlar_xonasi = yuzlar_xonasini_aniklovchi(uchxonali_son)
# print(f"Uchxonali sonning yuzlar xonasidagi raqami: {yuzlar_xonasi}")
# print(yuzlar_xonasi)


# 10.
def birliklar_honasidan(son):
    a = son // 10
    return a 

def onliklar_honasidan(son):
    b = son % 10
    return b 

def finish():
    son = int(input("Son kirit "))
    if son > 1000 or son < 99:
        print("Faqat 3 xonali son kiriting ")








