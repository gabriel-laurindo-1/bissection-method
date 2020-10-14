import math


def base_function(x):
    # Define f(x) function
    fx = (1/48)*(693*x**6-945*x**4+315*x**2-15)
    return fx


def k_estimated(a, b, tol):
    # formula para estimar o numero de interacoes
    return (math.log10(b-a)-math.log10(tol)/math.log10(2))


def bissection_method(a, b, tol):
    i = 0
    if b-a < tol:  # se o intervalo a b for menor q a precisao o programa acaba pegando o valor medio de a b
        x = (a+b)/2
        return {'k': 0, 'root': x}
    else:
        while True:
            i += 1  # incrementa o contador para medir o numero de iteracoes
            x = (a+b)/2  # pega x como o ponto central do intervalo a b
            fxa = base_function(a)  # calcula fx no ponto a
            fxb = base_function(b)  # calcula fx no ponto b
            fx = base_function(x)  # calcula fx no ponto x
            if fx == 0.0:  # se fx de x for menor q a precisao o programa acabar pegando x como resposta
                return {'k': 0, 'root': x}
            elif fxa*fx < 0:  # verifica se houve troca de sinal no valor de y a de a para x, se sim x e novo b
                b = x
            elif fxa*fx > 0:  # caso contrario x e o novo a
                a = x
            if b-a < tol:  # se o intervalo a b for menor q a precisao o programa acaba pegando o valor medio de a b
                x = (a + b) / 2
                return {'k': i, 'root': x}
