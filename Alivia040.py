def hitung_determinan_3x3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) -
            m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) +
            m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def invers_matriks_3x3(matriks):
    if len(matriks) != 3 or len(matriks[0]) != 3:
        raise ValueError("Fungsi ini khusus untuk matriks berordo 3x3!")

    det = hitung_determinan_3x3(matriks)
    
    if det == 0:
        raise ValueError("Matriks singular (Determinan = 0), tidak memiliki invers!")

    kofaktor = [
        [
            (matriks[1][1] * matriks[2][2] - matriks[1][2] * matriks[2][1]),
            -(matriks[1][0] * matriks[2][2] - matriks[1][2] * matriks[2][0]),
            (matriks[1][0] * matriks[2][1] - matriks[1][1] * matriks[2][0])
        ],
        [
            -(matriks[0][1] * matriks[2][2] - matriks[0][2] * matriks[2][1]),
            (matriks[0][0] * matriks[2][2] - matriks[0][2] * matriks[2][0]),
            -(matriks[0][0] * matriks[2][1] - matriks[0][1] * matriks[2][0])
        ],
        [
            (matriks[0][1] * matriks[1][2] - matriks[0][2] * matriks[1][1]),
            -(matriks[0][0] * matriks[1][2] - matriks[0][2] * matriks[1][0]),
            (matriks[0][0] * matriks[1][1] - matriks[0][1] * matriks[1][0])
        ]
    ]

    adjoin = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            adjoin[j][i] = kofaktor[i][j]

    invers = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3): 
            invers[i][j] = round(adjoin[i][j] / det, 4)

    return invers

def transpose_matriks_3x3(matriks):
    if len(matriks) != 3 or len(matriks[0]) != 3:
        raise ValueError("Fungsi ini khusus untuk matriks berordo 3x3!")
        
    hasil = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    for i in range(3):
        for j in range(3):
            hasil[j][i] = matriks[i][j]
            
    return hasil