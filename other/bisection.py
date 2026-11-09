import math
e,r,Is,Vt=5.0,1000.0,1e-12,25e-3
def f(V):
    return (e-V)/r-Is*(math.exp(V/Vt)-1)
def chia_doi(f,a,b,tol):     #tol(tolerance):sai số cho phép
    if f(a)*f(b)>=0:
        raise ValueError("f(a),f(b) phải trái dấu")
    # Sau n bước chia thì độ dài là: (a-b)/2^n
    # (a-b)/2^n <= tol suy ra n>=log2((a-b)/tol)
    n=math.ceil(math.log2((b-a)/tol))
    print(f"Số bước cần: {n}")
    for i in range(1,n+1):
        m=(a+b)/2
        print(f"{i}: a={a:.6f} b={b:.6f} m={m:.6f} f(m)={f(m):+.4e}")
        if f(a)*f(m)<0:
            b=m
        else:
            a=m
    return a,b
a,b=chia_doi(f,0.5,0.7,1e-3)
v=(a+b)/2
print(f"Khoảng chứa nghiệm:({a},{b})")
print(f"V={v}")