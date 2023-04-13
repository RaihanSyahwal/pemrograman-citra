import cv2 

image_3chan = cv2.imread('images.jpg') 
image_3chan_copy= image_3chan.copy()
cv2.imshow( 'Original image' , image_3chan )
cv2.waitKey(0) 
cv2.destroyAllWindows()

gray_image = cv2.cvtColor(image_3chan,cv2.COLOR_BGR2GRAY) 
ret,binary_im = cv2.threshold(gray_image,250,255,cv2.THRESH_BINARY) 
cv2.imshow( 'binary image' , binary_im )
cv2.waitKey(0) 
cv2.destroyAllWindows()

contours_list,hierarchy = cv2.findContours(binary_im,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
print('Hierarchy information of all contours:')
print (hierarchy)

for i in range(0, len(contours_list)):
    contour_info= hierarchy[0][i, :]
    print('Hierarchy information of current contour:')
    print(contour_info)
    if contour_info[2]==-1 and contour_info[3]==-1: # no parent, no child
        with_contours = cv2.drawContours(image_3chan_copy,contours_list,i,[0,255,0],thickness=3)
        print('Bolt contour is detected')
    if contour_info[2]==-1 and contour_info[3]!=-1: # no child but parent is present
        with_contours = cv2.drawContours(with_contours,contours_list,i, [0,0,255],thickness=3)
        print('Hole of nut is detected')
        
cv2.imshow( 'Contours marked on RGB image' , with_contours )
cv2.waitKey(0) 
cv2.destroyAllWindows()