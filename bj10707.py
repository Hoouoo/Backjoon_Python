A = int(input()) # X사 1리터 당 A엔
B = int(input()) # Y사의 기본요금
C = int(input()) # Y사의 기본 제공 리터
D = int(input()) # Y사의 기본 제공 초과 시 1리터당 부과되는 금액
P = int(input()) # 사용랑 P
X = A * P
Y = (D * (P-C)) + B if (D*(P-C)) > 0 else B
print(min(X, Y))