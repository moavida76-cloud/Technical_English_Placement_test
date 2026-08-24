import streamlit as st
import random

st.set_page_config(page_title="Technical English Placement Test", page_icon="💻", layout="centered")

RAW_QUESTIONS = [
    {"prompt": "1. Complete: 'Before pushing your code, you should _____ your changes locally.'", "options": ["commit", "merge", "delete", "break"], "correct_idx": 0, "explanation": "'Commit' guarda los cambios en el repositorio local.", "level": "Junior"},
    {"prompt": "2. What does 'deprecated' mean in software development?", "options": ["Critical for security.", "Recommended for new projects.", "Being phased out and shouldn't be used.", "Runs faster than normal."], "correct_idx": 2, "explanation": "'Deprecated' indica que algo está obsoleto.", "level": "Junior"},
    {"prompt": "3. [Passive Voice] 'The bug _____ yesterday by the QA team.'", "options": ["was found", "is finding", "found", "has find"], "correct_idx": 0, "explanation": "Voz pasiva en pasado simple ('was found').", "level": "Junior"},
    {"prompt": "4. [Interview] How do you politely explain your current role?", "options": ["I am responsible for maintaining the frontend code.", "I am make the HTML pages.", "My job is do CSS style.", "I have responsibility to writing code."], "correct_idx": 0, "explanation": "'I am responsible for + [verbo -ing]' es la forma correcta.", "level": "Junior"},
    {"prompt": "5. What is 'responsive design'?", "options": ["Website that answers emails.", "Design that adapts smoothly to different screen sizes.", "Website built only for desktop.", "Backend query style."], "correct_idx": 1, "explanation": "Adapta la interfaz a distintas pantallas.", "level": "Junior"},
    {"prompt": "6. CSS: 'The button is hidden because its property is set to _____.'", "options": ["display: none", "view: false", "hide: true", "show: off"], "correct_idx": 0, "explanation": "'display: none' oculta el elemento.", "level": "Junior"},
    {"prompt": "7. Standup: 'Yesterday I _____ on fixing the authentication module.'", "options": ["work", "was worked", "worked", "have work"], "correct_idx": 2, "explanation": "Pasado simple ('worked').", "level": "Junior"},
    {"prompt": "8. What does 'pull request' (PR) mean?", "options": ["Request to download a file.", "Proposal to merge code changes into a main repo.", "Server error message.", "Database query."], "correct_idx": 1, "explanation": "Propuesta para integrar cambios de código.", "level": "Junior"},
    {"prompt": "9. [Interview] 'What tools do you use for version control?'", "options": ["I am using Git every day for manage code.", "I mainly use Git and GitHub to manage my codebase.", "I use Git for make save files.", "I have used Git for store my pictures."], "correct_idx": 1, "explanation": "Respuesta profesional y bien estructurada.", "level": "Junior"},
    {"prompt": "10. 'The application is running _____ port 8080.'", "options": ["in", "at", "on", "under"], "correct_idx": 2, "explanation": "Se usa 'on' para puertos ('on port 8080').", "level": "Junior"},
    {"prompt": "11. What is the meaning of 'to roll back'?", "options": ["Deploy code to production.", "Revert software to a previous stable version.", "Scroll down rapidly.", "Encrypt passwords."], "correct_idx": 1, "explanation": "'Roll back' es restaurar a una versión previa.", "level": "Mid"},
    {"prompt": "12. [Passive Voice] 'All sensitive user data _____ before being stored.'", "options": ["must encrypt", "must be encrypted", "must encrypts", "must being encrypted"], "correct_idx": 1, "explanation": "Voz pasiva con modal ('must be + participio').", "level": "Mid"},
    {"prompt": "13. [Interview] How do you explain a past failure?", "options": ["It was completely the client's fault.", "We hit a roadblock, but I learned how to handle edge cases better.", "I don't remember any mistake.", "My team broke the code."], "correct_idx": 1, "explanation": "'Hit a roadblock' y mostrar aprendizaje es clave.", "level": "Mid"},
    {"prompt": "14. What does 'refactoring' code mean?", "options": ["Rewrite in another language.", "Restructuring existing code without changing external behavior.", "Fixing syntax errors.", "Adding new features."], "correct_idx": 1, "explanation": "Mejora la estructura interna sin cambiar comportamiento.", "level": "Mid"},
    {"prompt": "15. 'If we _____ the database query, response time will decrease.'", "options": ["optimize", "optimized", "will optimize", "optimizing"], "correct_idx": 0, "explanation": "Primer condicional (If + presente simple).", "level": "Mid"},
    {"prompt": "16. 'We spent hours trying to figure out the bug.' 'Figure out' means:", "options": ["Delete", "Discover or solve", "Report", "Ignore"], "correct_idx": 1, "explanation": "'Figure out' es descubrir o resolver.", "level": "Mid"},
    {"prompt": "17. 'Please make sure to catch potential exceptions.' 'Catch' means:", "options": ["Hold the server.", "Handle errors gracefully during execution.", "Create a variable.", "Suppress errors."], "correct_idx": 1, "explanation": "Manejo de errores con try/catch.", "level": "Mid"},
    {"prompt": "18. [Passive Voice] 'The new feature _____ by the staging server right now.'", "options": ["is being processed", "is processing", "was process", "has processed"], "correct_idx": 0, "explanation": "Presente continuo pasivo ('is being + participio').", "level": "Mid"},
    {"prompt": "19. [Interview] How to discuss salary expectations?", "options": ["I want a lot of money.", "Based on my experience and research, I am looking for a range between $X and $Y.", "Give me maximum salary.", "I don't care about salary."], "correct_idx": 1, "explanation": "Forma profesional con rango estimado.", "level": "Mid"},
    {"prompt": "20. HTTP 404 status code means:", "options": ["Found", "Not found", "Created", "Forbidden"], "correct_idx": 1, "explanation": "HTTP 404 = Not Found.", "level": "Mid"},
    {"prompt": "21. [Passive Voice] 'Had the security patch _____ in time, the breach could have been prevented.'", "options": ["deployed", "been deployed", "being deployed", "be deploy"], "correct_idx": 1, "explanation": "Inversión condicional pasada pasiva.", "level": "Senior"},
    {"prompt": "22. What does 'out of the box' imply?", "options": ["Requires complex setup.", "Functionality that works immediately without extra configuration.", "Memory overflow error.", "Highly experimental."], "correct_idx": 1, "explanation": "Funciona listo para usar sin configuración.", "level": "Senior"},
    {"prompt": "23. [Interview] Senior question about tech stack choices:", "options": ["Why React? Vue is better.", "Could you walk me through the trade-offs you considered when choosing React?", "Why React instead of superior tools?", "Who decided this?"], "correct_idx": 1, "explanation": "Evalúa criterios técnicos y trade-offs.", "level": "Senior"},
    {"prompt": "24. What does 'scope creep' refer to in Scrum?", "options": ["Uncontrolled growth in project requirements.", "Developer pushing to main.", "Moving tasks to sprint.", "Speed of paying technical debt."], "correct_idx": 0, "explanation": "Crecimiento no planificado del proyecto.", "level": "Senior"},
    {"prompt": "25. Post-mortem incident report (mixed conditional):", "options": ["If we had refactored the legacy code last month, our app would be much faster today.", "If we refactor, it would be fast.", "If we would have refactored, app will be faster.", "If we refactored, app was faster."], "correct_idx": 0, "explanation": "Condicional mixto (Causa pasada -> Efecto presente).", "level": "Senior"},
    {"prompt": "26. 'We need to _____ and drop non-essential features.'", "options": ["hit the sack", "bite the bullet", "touch base", "reinvent the wheel"], "correct_idx": 1, "explanation": "'Bite the bullet' = tomar una decisión difícil.", "level": "Senior"},
    {"prompt": "27. What does 'technical debt' refer to?", "options": ["Money owed to hosting providers.", "Implied cost of additional rework caused by choosing an easy solution now.", "Salary paid to juniors.", "Software licenses."], "correct_idx": 1, "explanation": "Costo diferido por tomar atajos en código.", "level": "Senior"},
    {"prompt": "28. [Interview] Handling system design disagreement:", "options": ["Insist my approach is standard.", "Acknowledge alternative patterns and defend choice using metrics.", "Change opinion immediately.", "Refuse to discuss."], "correct_idx": 1, "explanation": "Defender decisiones con métricas y datos.", "level": "Senior"},
    {"prompt": "29. What does 'decoupling' mean?", "options": ["Disconnect power.", "Separating components so changes in one don't force changes in another.", "Merge backend and frontend.", "Delete dependencies."], "correct_idx": 1, "explanation": "Desacoplar componentes independientes.", "level": "Senior"},
    {"prompt": "30. [Passive Voice] 'Had microservices not been adopted, the platform _____ scalable enough.'", "options": ["won't be", "wouldn't have been", "isn't being", "had not been"], "correct_idx": 1, "explanation": "Tercer condicional en voz pasiva.", "level": "Senior"}
]

def prepare_questions():
    prepared = []
    letters = ["A", "B", "C", "D"]
    for q in RAW_QUESTIONS:
        opts = list(q["options"])
        correct_text = opts[q["correct_idx"]]
        random.shuffle(opts)
        new_correct_letter = letters[opts.index(correct_text)]
        formatted_options = [f"{letters[i]}) {opts[i]}" for i in range(len(opts))]
        prepared.append({
            "prompt": q["prompt"],
            "options": formatted_options,
            "correct": new_correct_letter,
            "explanation": q["explanation"],
            "level": q["level"]
        })
    return prepared

if "current_q" not in st.session_state:
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.student_name = ""
    st.session_state.started = False
    st.session_state.finished = False
    st.session_state.answered = False
    st.session_state.selected_option = None

st.title("💻 Technical English Placement Test")
st.caption("Evaluación de nivel de inglés técnico para Programadores")

if not st.session_state.started:
    st.subheader("Bienvenido/a a la prueba de nivel")
    name = st.text_input("Ingresa el nombre completo del alumno:")
    if st.button("Iniciar Evaluación 🚀", type="primary"):
        if name.strip():
            st.session_state.student_name = name.strip()
            st.session_state.questions = prepare_questions()
            st.session_state.started = True
            st.rerun()
        else:
            st.warning("Ingresa un nombre antes de comenzar.")

elif st.session_state.started and not st.session_state.finished:
    q_index = st.session_state.current_q
    question = st.session_state.questions[q_index]
    total_q = len(st.session_state.questions)

    st.progress(q_index / total_q, text=f"Pregunta {q_index + 1} de {total_q} ({question['level']})")
    st.markdown(f"### {question['prompt']}")

    selected = st.radio("Selecciona la opción correcta:", question["options"], key=f"q_{q_index}", disabled=st.session_state.answered)

    if not st.session_state.answered:
        if st.button("Confirmar Respuesta", type="primary"):
            st.session_state.selected_option = selected[0]
            st.session_state.answered = True
            if st.session_state.selected_option == question["correct"]:
                st.session_state.score += 1
            st.rerun()

    if st.session_state.answered:
        if st.session_state.selected_option == question["correct"]:
            st.success("¡Respuesta Correcta! 🎉")
        else:
            st.error(f"Incorrecto. La respuesta era la **{question['correct']}**.")
        st.info(f"💡 **Explicación:** {question['explanation']}")

        if st.button("Siguiente Pregunta ➡️"):
            st.session_state.answered = False
            st.session_state.selected_option = None
            if st.session_state.current_q + 1 < total_q:
                st.session_state.current_q += 1
            else:
                st.session_state.finished = True
            st.rerun()

elif st.session_state.finished:
    total_q = len(st.session_state.questions)
    score = st.session_state.score
    percentage = (score / total_q) * 100

    st.balloons()
    st.header("📊 Resultados del Diagnóstico")
    st.markdown(f"**Alumno:** {st.session_state.student_name}")
    st.markdown(f"**Puntuación:** {score} / {total_q} (`{percentage:.1f}%`)")
    st.divider()

    if percentage < 45:
        cefr, course, desc, badge = "A2 - Elementario", "Inglés Técnico Inicial", "Reforzar bases, comandos y git.", "red"
    elif percentage < 75:
        cefr, course, desc, badge = "B1/B2 - Intermedio", "Inglés para Developers", "Daily standups, entrevistas y PRs.", "orange"
    else:
        cefr, course, desc, badge = "C1/C2 - Avanzado", "Inglés para Tech Leads", "Liderazgo, trade-offs y arquitectura.", "green"

    st.markdown(f"**Nivel Estimado:** :{badge}[{cefr}]")
    st.markdown(f"**Curso Asignado:** `{course}`")
    st.markdown(f"**Enfoque Recomendado:** {desc}")
    st.divider()

    if st.button("Reiniciar Evaluación 🔄"):
        st.session_state.clear()
        st.rerun()
   
          
    
