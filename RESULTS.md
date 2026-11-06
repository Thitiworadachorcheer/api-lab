# API lab results

## Part 0
- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: The Fast Calzone
- Step 0.12, results of the three runs without a session (optional): ไม่ผ่านทั้ง 3 ครั้ง โดยล้มเหลวที่คำขอล็อกอินได้สถานะ 401 แทนที่จะเป็น 200 เพราะไม่มี session คอยเก็บ cookie AWSALB ทำให้ load balancer ส่งคำขอไปยังคนละเซิร์ฟเวอร์ที่ยังไม่รู้จักผู้ใช้
- Step 0.16, blocks of "how many of the three tools are excluded": แบ่งออกเป็น 4 blocks ได้แก่ - - 
ไม่ตัดเครื่องมือออกเลย ([]), ตัดออก 1 ชิ้น (เช่น ["Knife"] หรือ ["Scissors"]), ตัดออก 2 ชิ้น (เช่น ["Knife", "Pizza cutter"]), และตัดออก 3 ชิ้นครบทุกชิ้น (["Knife", "Pizza cutter", "Scissors"])

Defect report
Title: การตัดเครื่องมือทำพิซซ่าออกทั้งหมดส่งผลให้เซิร์ฟเวอร์ตอบกลับ 500 แทนที่จะเป็น 400
Request: POST /api/pizza พร้อม header Authorization และ body {"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}
Expected result: สถานะ 400 Bad Request พร้อมข้อความ error ในรูปแบบ JSON แจ้งว่าไม่สามารถจัดหาพิซซ่าตามเงื่อนไขได้
Actual result: สถานะ 500 Internal Server Error พร้อม body ว่างเปล่า
Severity: ปานกลาง เพราะแม้จะไม่ทำให้ระบบล่มทั้งเซิร์ฟเวอร์ แต่การตอบ 500 ทำให้ฝั่งแอปพลิเคชันเข้าใจผิดว่าเป็นข้อผิดพลาดภายในของเซิร์ฟเวอร์ แทนที่จะแจ้งเตือนผู้ใช้ว่าเงื่อนไขเป็นไปไม่ได้