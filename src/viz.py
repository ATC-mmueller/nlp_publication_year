from sklearn.metrics import confusion_matrix
from matplotlib import pyplot as plt
import seaborn as sns

def plot_confusion_matrix(y_test : list, 
                          y_pred : list, 
                          title = 'Confusion Matrix', 
                          decades = []) -> None:
    decades.sort()
    fig, ax = plt.subplots(figsize = (12,10))
    sns.heatmap(data = confusion_matrix(y_test, y_pred), 
                cmap = 'YlOrBr',
                annot=True,
                fmt = 'd',
                xticklabels = decades,
                yticklabels = decades
               )
    plt.title(title, fontsize=20, pad=15.0)
    plt.xlabel('Predicted label', fontsize=14)
    plt.ylabel('True label', fontsize=14)
    plt.xticks(rotation=60)
    #plt.savefig('viz/sns_heatmap_iteration_3.png')
    plt.show()
    
def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(40, 30))
    # Display image
    plt.imshow(wordcloud) 
    # No axis details
    plt.axis("off");
    
from wordcloud import WordCloud
def create_wordcloud(text : str, stopwords = []):
    wordcloud = WordCloud(width= 3000,
                          height = 2000,
                          random_state=1,
                          background_color='salmon',
                          colormap='Pastel1',
                          collocations=False,
                          stopwords = stopwords).generate(text)
    plot_cloud(wordcloud)