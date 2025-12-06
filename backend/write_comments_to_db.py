import json                                                                                                                         
from sqlmodel import SQLModel, Session                                                                                              
from app.models.models import Comment                                                                                               
from app.database import engine                                                                                                     
                                                                                                                                    
def main():                                                                                                                         
    """                                                                                                                             
    Reads comments from a JSON file and writes them to the database.                                                                
    """                                                                                                                             
    SQLModel.metadata.create_all(engine)                                                                                            
                                                                                                                                    
    with Session(engine) as session:                                                                                                
        with open('consultations_comments.json', 'r', encoding='utf-8') as f:                                                       
            comments_data = json.load(f)                                                                                            
                                                                                                                                    
        for comment_data in comments_data:                                                                                          
            # The id field is auto-incrementing, so we don't need to provide it.                                                    
            comment_data["id"] = 0
            comment_data.pop('lp', None)                                                                                            
            comment = Comment.model_validate(comment_data)                                                                          
            comment.id = None
            session.add(comment)                                                                                                    
                                                                                                                                    
        session.commit()                                                                                                            
                                                                                                                                    
    print(f"Successfully wrote {len(comments_data)} comments to the database.")                                                     
                                                                                                                                    
if __name__ == "__main__":                                                                                                          
    main()                                                                                                                          
