# Image Upscaling Tool

## 專案介紹
本專案基於 [Real-ESRGAN](https://github.com/ai-forever/Real-ESRGAN) 所開發，旨在對圖片進行畫質增強處理。  
執行 `main.py` 後，系統將對輸入資料夾中的所有圖片，進行畫質增強，並將處理後的結果輸出至輸出資料夾中。

## 專案用法

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
將欲提升解析度的圖片檔案放入 `image/` 資料夾中，或另外指定輸入資料夾。

#### 5. 執行主程式
執行 `main.py`，並可透過參數設定模型倍率、輸入與輸出路徑等選項。

```bash
參數介紹
    --factor        可選，放大倍率
    --input         可選，輸入資料夾路徑
    --output        可選，輸出資料夾路徑
    --overwrite     可選，是否覆寫檔案

參數數值範圍與預設值
    --factor        [2, 4, 8]             預設為 2
    --input         路徑字串               預設為 "./image"
    --output        路徑字串               預設為 "./output"
    --overwrite     旗標（無需數值）        預設為 False
```

## 注意事項
> 由於 [Real-ESRGAN](https://github.com/ai-forever/Real-ESRGAN) 的原始碼相對較舊，為使其能順利執行並符合現今的執行環境，本專案對其程式碼進行了少許的調整與修改，並且已將修改後的原始碼直接包含於本專案中。但需特別聲明，該程式碼之著作權仍歸屬於 [Real-ESRGAN](https://github.com/ai-forever/Real-ESRGAN) 專案原作者所有。
