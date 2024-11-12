#x = [0.5, 0.75, 1, 1.5, 2, 2.5, 3]
#x = [0, 3, 35]
#y = [-2.8, -0.6, 1, 3.2, 4.8, 6, 7]
#y = [13, 15, 20]
def coef(a, b, c, det):
    dA = a/det
    dB = b/det
    dC = c/det
    return print(f"f(x) = ({dC:.2f})x² + ({dB:.2f})x + ({dA:.2f})")

def sum(x, y):
    ls = []
    s_0 = s_x1 = s_x2 = s_x3 = s_x4 = s_a =s_b = s_c = 0
    for i in range(0, len(x)):
        s_0 = s_0 + 1
        s_x1 = s_x1+  (x[i])
        s_x2 = s_x2+  ( (x[i])*(x[i]) )
        s_x3 = s_x3+  ( (x[i])*(x[i])*(x[i]) )
        s_x4 = s_x4+  ( (x[i])*(x[i])*(x[i])*(x[i]) )
        s_a = s_a + (y[i]) #yk
        s_b = s_b + ( (x[i] * y[i]) ) #xy
        s_c = s_c + ( ( (x[i]*x[i]) * y[i] ) ) #x²y
    ls = [s_0, s_x1, s_x2, s_x3, s_x4, s_a, s_b, s_c] # a5, b6, c7
    return ls

def new_det_geral(x, y):
    l = sum(x, y)
    d_i = (l[0] * l[2] * l[4]) + (l[1] * l[3] * l[2]) + (l[2] * l[1] * l[3])
    d_v = (l[1] * l[1] * l[4]) + (l[0] * l[3] * l[3]) + (l[2] * l[2] * l[2])
    df = (d_i - d_v)
    return df

def new_det_A(x, y):
    l = sum(x, y)
    d_i = (l[5] * l[2] * l[4]) + (l[1] * l[3] * l[7]) + (l[2] * l[6] * l[3])
    d_v = (l[1] * l[6] * l[4]) + (l[5] * l[3] * l[3]) + (l[2] * l[2] * l[7])
    df = (d_i - d_v)
    return df

def new_det_B(x, y):
    l = sum(x, y)
    d_i = (l[0] * l[6] * l[4]) + (l[5] * l[3] * l[2]) + (l[2] * l[1] * l[7])
    d_v = (l[5] * l[1] * l[4]) + (l[0] * l[3] * l[7]) + (l[2] * l[6] * l[2])
    df = (d_i - d_v)
    return df

def new_det_C(x, y):
    l = sum(x, y)
    d_i = (l[0] * l[2] * l[7]) + (l[1] * l[6] * l[2]) + (l[5] * l[1] * l[3])
    d_v = (l[1] * l[1] * l[7]) + (l[0] * l[6] * l[3]) + (l[5] * l[2] * l[2])
    df = (d_i - d_v)
    return df

def main():
    lx = []
    ly = []

    def val_points():
        q = int(input("Quantidade de pontos: "))
        
        for i in range(0, q):
            lx.insert(i, float(input(f" - X{i}: ")))
            ly.insert(i, float(input(f" - Y{i}: ")))

    def mostra_det():
        a = new_det_A(lx, ly)
        b = new_det_B(lx, ly)
        c = new_det_C(lx, ly)
        d = new_det_geral(lx, ly)
        print(f"Determinante = {d:.2f}")
        coef(a, b, c, d)
    val_points()
    mostra_det()

main()