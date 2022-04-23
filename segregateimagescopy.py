import os
import face_recognition
import cv2
import os.path

i = 1
index = 0
visited = set()
existingImages =  []
sourceFolder = "G:/testimages/"
destFolder = "G:/"
images = os.listdir(sourceFolder)

def recog(letsmatch):
	
	global i
	count = 1
	address = os.path.join(destFolder, 'folder{}'.format(i))

	for image in images:
		index = images.index(image)  
		if index not in existingImages:
			pata = os.path.join(sourceFolder, image)
			photo = cv2.imread(pata)
			current_image = face_recognition.load_image_file(sourceFolder + image)
			try:
				current_image_encoded = face_recognition.face_encodings(current_image)[0]
			except IndexError as e:
				print(e)
	  
			result = face_recognition.compare_faces([letsmatch], current_image_encoded)
			if result[0] == True:
				filepath = address + '/' + str(count) + '.jpg'
				if pata not in visited:
					if os.path.isdir(address) == False:
						os.mkdir(address)
						i += 1	
					visited.add(pata)
					existingImages.append(index)
					cv2.imwrite(filepath, photo)
				else:
					continue
			else:
				pass
			count += 1
		
for image in images:
	image_to_be_recognized = face_recognition.load_image_file(sourceFolder + image)
	image_to_be_recognized_encoded = face_recognition.face_encodings(image_to_be_recognized)[0]
	recog(image_to_be_recognized_encoded)
    
cv2.waitKey(0)
cv2.destroyAllWindows()	
