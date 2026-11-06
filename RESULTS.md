# API lab results

## Part 0
- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: The Fast Calzone
- Step 0.12, results of the three runs without a session (optional): ไม่ผ่านทั้ง 3 ครั้ง โดยล้มเหลวที่คำขอล็อกอินได้สถานะ 401 แทนที่จะเป็น 200 เพราะไม่มี session คอยเก็บ cookie AWSALB ทำให้ load balancer ส่งคำขอไปยังคนละเซิร์ฟเวอร์ที่ยังไม่รู้จักผู้ใช้