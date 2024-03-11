function [autovalor, autovetor] = maior_eigen(matriz, vetor_inicial, tolerancia, iteracoes_maximas)
    // Através do método da potência, retorna o maior autovalor de uma dada matriz e seu autovetor correspondente
    autovetor = vetor_inicial
    autovalor = 0
    for k=1:iteracoes_maximas
        vetor_produto = matriz * autovetor // y = Ax
        norma_vetor_produto = sqrt(sum(vetor_produto .^ 2)) // ||y||
        autovetor = vetor_produto / norma_vetor_produto // x = y / ||y||
        autovalor_atual = autovetor' * vetor_produto //  lambda = x.T * y
        if abs(autovalor - autovalor_atual) < tolerancia then
            return
        end
        autovalor = autovalor_atual
    end
    disp('Quantidade máxima de iterações excedida.')
    return
endfunction


// matriz (A)
matriz = [
    1, 0, 0
    2, 3, 0
    3, 4, 2
]
// vetor inicial (x)
vetor_inicial = [1; 1; 1]
[autovalor, autovetor] = maior_eigen(matriz=matriz, vetor_inicial=vetor_inicial, tolerancia=1e-10, iteracoes_maximas=1000)
disp(autovalor) // 3.0021537
disp(autovetor) // [9.399D-10, 0.2427675, 0.9700845]
