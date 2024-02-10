from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    links = [
        {
            'url': 'https://hotmart.com/pt-br/marketplace/produtos/criacao-de-mapas-profissionais-com-r/X78799898R',
            'title': 'Criação de Mapas Geoespaciais com R',
            'description': 'Scripts Prontos, Etapas Explicadas e Exemplos Práticos',
            'image': 'https://cdn.beacons.ai/user_content/3aZQQmoXXJfL8Bkg8L3zoRioGJ12/referenced_images/7ca79faa-4ae4-497b-9b5b-c065e0e18f4d__link-in-bio__links-block__home__79d34ef1-ceae-47e1-9526-87674111ddda__3689255d-7b70-4dc7-b6d6-78e84d272fb4__22aed620-a705-4cbb-bf28-56325cd9cbe7.webp?t=1707500171786'
        },
        {
            'url': 'https://hotmart.com/pt-br/marketplace/produtos/transforme-sua-rotina-profissional_-automatizando-tarefas-com-programacao-em-r/F89921306F',
            'title': 'Introdução ao R',
            'description': 'Scripts Prontos, Etapas Explicadas e Exemplos Práticos',
            'image': 'https://cdn.beacons.ai/user_content/3aZQQmoXXJfL8Bkg8L3zoRioGJ12/link_images/bf29106d-b689-42a4-a6fa-8dfa86c810b4.png'
        },
         {
            'url': 'https://hotmart.com/pt-br/marketplace/produtos/clube-de-assinaturas-da-universidade-dos-dados/Y79687647W?ref=P90785750U',
            'title': 'Clube de Assinaturas da Universidade dos Dados',
            'description': '🌟 Quer aprender algo novo toda semana? Desenvolva suas habilidades profissionais em Python, PowerBI e resolução de problemas de negócios! Clique no link da bio! 📚 Aproveite essa super oportunidade com nossa parceria! 🌟',
            'image': 'https://cdn.beacons.ai/user_content/3aZQQmoXXJfL8Bkg8L3zoRioGJ12/link_images/6f9c591d-aa4e-4c4d-862d-15019d7e8628.png'
        },

        {
            'url': 'https://www.instagram.com/roch.dta/',
            'title': 'Instagram',
            'description': 'Siga-me no Instagram',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/1024px-Instagram_icon.png'
        }
        # Adicione mais links conforme necessário
    ]
    return render_template('index.html', links=links)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
