from xml.dom import minidom
def get_xml_data(f):
    Load_XML = minidom.parse(f)

    #filename
    filename = Load_XML.getElementsByTagName("filename")
    filename = filename.item(0).childNodes.item(0).data

    #path
    path = Load_XML.getElementsByTagName("path")
    path = path.item(0).childNodes.item(0).data

    #size
    size   = Load_XML.getElementsByTagName("size")
    width  = size.item(0).getElementsByTagName('width').item(0).childNodes.item(0).data
    height = size.item(0).getElementsByTagName('height').item(0).childNodes.item(0).data
    depth  = size.item(0).getElementsByTagName('depth').item(0).childNodes.item(0).data

    object   = Load_XML.getElementsByTagName("object")
    testtype = object.item(0).getElementsByTagName('name').item(0).childNodes.item(0).data
    xmin     = object.item(0).getElementsByTagName('bndbox').item(0).getElementsByTagName('xmin').item(0).childNodes.item(0).data
    ymin     = object.item(0).getElementsByTagName('bndbox').item(0).getElementsByTagName('ymin').item(0).childNodes.item(0).data
    xmax     = object.item(0).getElementsByTagName('bndbox').item(0).getElementsByTagName('xmax').item(0).childNodes.item(0).data
    ymax     = object.item(0).getElementsByTagName('bndbox').item(0).getElementsByTagName('ymax').item(0).childNodes.item(0).data
    return filename,path,width,height,depth, testtype,xmin,ymin,xmax,ymax

data=[]
with open("train.txt") as f:
    d = f.read().split('\n')
    for dd in d:
        data.append(get_xml_data("liveuxml/" + dd +".xml"))

with open("flickr_logos_27_dataset_training_set_annotation.txt","w") as w:
    for d in data:
        w.write(d[0] + "\t" + "liveu" + "\t" + "1" + "\t" + d[6] + "\t" + d[7] + "\t" + d[8] + "\t" + d[9] + "\n")

with open("flickr_logos_27_dataset_query_set_annotation.txt","w") as w:
    for d in data:
        w.write(d[0] + "\t" + "None" + "\n")

#2514220918.jpg Yahoo 6 1   69 342 157
#386891249.jpg  Yahoo 6 156 10 310 49
#[vijay@localhost DeepLogo]$ cat flickr_logos_27_dataset/flickr_logos_27_dataset_training_set_annotation.txt

#4283515483.jpg,352,8,496,72,24
#2921061781.jpg,103,8,190,60,12
#[vijay@localhost DeepLogo]$ cat flickr_logos_27_dataset/flickr_logos_27_dataset_training_set_annotation_cropped.txt

#3490185235.jpg	none
#3490913574.jpg	none
#[vijay@localhost DeepLogo]$ cat flickr_logos_27_dataset/flickr_logos_27_dataset_query_set_annotation.txt

#2531530868.jpg,37,139,360,285,16
#[vijay@localhost DeepLogo]$ cat flickr_logos_27_dataset/flickr_logos_27_dataset_test_set_annotation_cropped.txt