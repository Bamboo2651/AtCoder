import time
 
for i in range(5):
    print(f"進捗: {i+1}/5", end="\r", flush=True)  # end="\r"で同じ行を上書き表示
    time.sleep(1)
 
print("\n処理完了", flush=True)