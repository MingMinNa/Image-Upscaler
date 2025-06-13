## Image Upscaling Tool

### 專案介紹
本專案基於 [Real-ESRGAN](https://github.com/ai-forever/Real-ESRGAN) 所開發，旨在對圖片進行畫質增強處理。執行 `main.py` 後，系統將自動讀取 `image` 資料夾中的所有圖片，進行畫質提升，並將處理後的結果輸出至 `output` 資料夾中。

---

### 專案用法

#### 1. 創建與開啟虛擬環境
使用下列指令建立虛擬環境，並啟用它（請將 `<venv_name>` 替換為自訂的環境名稱）
```bash
conda create -n <venv_name> python=3.12
conda activate <venv_name>
```
#### 2. 安裝相依套件
在虛擬環境中安裝所有必要的 Python 套件
```bash
pip install -r requirements.txt
```

#### 3. 下載模型權重
請將下載後的模型權重檔案放入專案根目錄下的 `weights/` 資料夾中。
#### 4. 放置輸入圖片
將欲提升解析度的圖片檔案放入 `image/` 資料夾中。
#### 5. 執行主程式
透過以下指令執行主程式 `main.py`，可使用 `--factor` 參數指定所需的模型倍率。
```bash
python main.py --factor <倍率>
```
---

### 注意事項
> 由於 [Real-ESRGAN](https://github.com/ai-forever/Real-ESRGAN) 的原始碼相對較舊，為使其能順利執行並符合現今的執行環境，本專案對其程式碼進行了少許的調整與修改。
為方便使用，已將修改後的原始碼直接包含於本專案中。但需特別聲明，該程式碼之著作權仍歸屬於 [Real-ESRGAN](https://github.com/ai-forever/Real-ESRGAN) 專案原作者所有。
