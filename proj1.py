reviews= [ "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]



good_review1 = "this product is really good"
good_review2 = "im impressed with its quality"
good_review3 = "the performance of this product is exellent"

first = good_review1[23:27]
loud_first = first.upper()
firstr = good_review1.replace("good", loud_first)
print(firstr)

second = good_review2 [3:13]
loud_second = second.upper()
secondr = good_review2.replace("impressed", loud_second)
print(secondr)

third = good_review3[35:44]
loud_third = third.upper()
thirdr = good_review3.replace("exellent", loud_third)

bad_reviews1 = "I had a bad exeperience with this product"
bad_reviews2 = "poor quality product"
bad_reviews3 = "the product was average"


firstv2 = bad_reviews1 [8:11]
loud_firstv2 =firstv2.upper()
firstv2r = bad_reviews1.replace("bad", loud_firstv2)

secondv2 = bad_reviews2 [0:5]
loud_secondv2 = secondv2.upper()
secondv2r = bad_reviews2.replace("poor", loud_secondv2)

thirdv2 = bad_reviews3 [16:23]
loud_thirdv2 = thirdv2.upper()
thirdv2r = bad_reviews3.replace("average", loud_thirdv2)






positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def count_words(positive_words,negative_words,reviews):
    positive_counter = 0
    negative_counter = 0
    for positive_word in positive_words:
        for review in reviews:
            if positive_word in review.lower():
                positive_counter +=1
        
    for negative_word in negative_words:
        for review in reviews:
            if negative_word in review.lower():
                negative_counter +=1            

    return positive_counter, negative_counter
   
print(count_words(positive_words,negative_words,reviews))


for review in reviews:
    last_space_index = review[:30].rfind(" ")
    print(review[:last_space_index] + "...")

