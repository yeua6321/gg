import ddddocr
import cv2

# 初始化检测器（关闭OCR功能，仅启用目标检测）
det = ddddocr.DdddOcr(det=True, ocr=False)

# 读取验证码图片
with open("2.png", 'rb') as f:
    image_bytes = f.read()

# 检测目标位置
poses = det.detection(image_bytes)
print("检测到的目标位置（bbox坐标）:", poses)

# 可视化结果：在图片上绘制检测框
im = cv2.imread("2.png")
for box in poses:
    x1, y1, x2, y2 = box
    im = cv2.rectangle(im, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=2)
    # 在框上方添加文本标签
    im = cv2.putText(im, f"({x1},{y1})", (x1, y1-10),
    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)




# 保存结果图片
cv2.imwrite("result_2.png", im)
print("结果已保存至 result_2.png")