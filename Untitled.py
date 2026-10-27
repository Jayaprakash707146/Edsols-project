#!/usr/bin/env python
# coding: utf-8

# In[29]:


from Arm_Lib import Arm_Device
import time
Arm = Arm_Device()
Arm.Arm_serial_servo_write6(90, 90, 90, 90, 90, 90,1000)
time.sleep(2.0)
Arm.Arm_serial_servo_write(1,90,1000)
Arm.Arm_serial_servo_write(2,90,1000)
Arm.Arm_serial_servo_write(3,6,1000)
Arm.Arm_serial_servo_write(4,90,1000)
Arm.Arm_serial_servo_write(5,90,1000)
Arm.Arm_serial_servo_write(6,90,1000)
time.sleep(2.0)
Arm.Arm_serial_servo_write(3,176,1000)
time.sleep(2.0)
Arm.Arm_serial_servo_write6(90, 91, 1, 176, 77, 68,1000)



# In[28]:





# In[18]:





# In[ ]:




