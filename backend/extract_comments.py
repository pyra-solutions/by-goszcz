import glob                                                                                                                         
import json                                                                                                                         
from bs4 import BeautifulSoup                                                                                                       
from dataclasses import dataclass, asdict                                                                                           
                                                                                                                                    
@dataclass                                                                                                                          
class Comment:                                                                                                                      
    consultation_id: str                                                                                                            
    lp: str                                                                                                                         
    question: str                                                                                                                   
    comment_text: str                                                                                                               
    author: str                                                                                                                     
    poll_number: str                                                                                                                
                                                                                                                                    
def extract_comments_from_file(file_path: str) -> list[Comment]:                                                                    
    comments = []                                                                                                                   
    consultation_id = file_path.split('/')[-1].replace('.html', '').replace('_', '/')                                               
                                                                                                                                    
    with open(file_path, 'r', encoding='utf-8') as f:                                                                               
        soup = BeautifulSoup(f, 'html.parser')                                                                                      
                                                                                                                                    
    table = soup.find('table', class_='konsultacje')                                                                                
    if not table or not table.tbody:                                                                                                
        return []                                                                                                                   
                                                                                                                                    
    for row in table.tbody.find_all('tr'):                                                                                          
        tds = row.find_all('td')                                                                                                    
        if len(tds) == 4:                                                                                                           
            lp = tds[0].get_text(strip=True)                                                                                        
            question = tds[1].get_text(strip=True)                                                                                  
            comment_text = tds[2].get_text(strip=True)                                                                              
            author_raw = tds[3].get_text(strip=True)                                                                                
                                                                                                                                    
            # Split author and poll number                                                                                          
            author_parts = author_raw.split('ankieta nr')                                                                           
            author = author_parts[0].strip()                                                                                        
            poll_number = author_parts[1].strip() if len(author_parts) > 1 else ''                                                  
                                                                                                                                    
            comments.append(Comment(                                                                                                
                consultation_id=consultation_id,                                                                                    
                lp=lp,                                                                                                              
                question=question,                                                                                                  
                comment_text=comment_text,                                                                                          
                author=author,                                                                                                      
                poll_number=poll_number                                                                                             
            ))                                                                                                                      
    return comments                                                                                                                 
                                                                                                                                    
def main():                                                                                                                         
    all_comments = []                                                                                                               
    file_paths = glob.glob('consultations/*.html')                                                                                  
                                                                                                                                    
    for file_path in file_paths:                                                                                                    
        print(f"Extracting comments from {file_path}...")                                                                           
        comments = extract_comments_from_file(file_path)                                                                            
        all_comments.extend(comments)                                                                                               
                                                                                                                                    
    # Save to a JSON file                                                                                                           
    output_filename = 'consultations_comments.json'                                                                                 
    with open(output_filename, 'w', encoding='utf-8') as f:                                                                         
        json.dump([asdict(c) for c in all_comments], f, indent=4, ensure_ascii=False)                                               
                                                                                                                                    
    print(f"Extracted {len(all_comments)} comments and saved to {output_filename}")                                                 
                                                                                                                                    
if __name__ == '__main__':                                                                                                          
    main()                                                                                                                          

