import requests
import pandas as pd
def fetch_reviews(page_url):
    reviews= []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Cookie': 'PHPSESSID=d8fb55206d28b61f'
    }
    response = requests.get(f"{page_url}", headers=headers)
    out=(response.json())
    reviews=out['entities']['REVIEWS']
    #print(out['REVIEWS']['userName'])

    extracted_info = []

    # Iterate through the dictionary and get required information
    for key, review in reviews.items():
        user_info = {'reviewID':review.get('reviewId'),'userName': review.get('userName'),'timestamp': review.get('timestamp'),'reviewText': review.get('reviewText'),'rating':review.get('ratingV2'),'dining/delivery type':review.get('experience')}
        extracted_info.append(user_info)
    return extracted_info

if __name__ == "__main__":
    restaurant_url = "https://www.zomato.com/webroutes/getPage?page_url=/chennai/secret-story-nungambakkam/reviews"# Replace with desired restaurant URL
    final_reviews=[]
    for i in range(1,85):
        page_url = f"https://www.zomato.com/webroutes/reviews/loadMore?sort=dd&filter=reviews-dd&res_id=20420088&page={i}"
        #reviews = fetch_reviews(restaurant_url)
        final_reviews.append(fetch_reviews((page_url)))
    print(final_reviews)
    flattened_reviews = [review for sublist in final_reviews for review in sublist]# Flatten the nested list into a single list of dictionaries
    df = pd.DataFrame(flattened_reviews) # Create a DataFrame
    csv_file = 'reviewszomato.csv'# Define the CSV file name
    df.to_csv(csv_file, index=False, encoding='utf-8')# Write the DataFrame to a CSV file
    print(f'Successfully written to {csv_file}')
    #save_to_csv(final_reviews, 'zomato_reviews_final.csv')

