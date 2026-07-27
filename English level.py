import streamlit as st

st.set_page_config(page_title="Technical English Placement Test", page_icon="💻", layout="centered")

QUESTIONS = [
    {"prompt": "1. Complete: 'Before pushing your code, you should _____ your changes locally.'", "options": ["A) commit", "B) merge", "C) delete", "D) break"], "correct": "A", "explanation": "'Commit' guarda los cambios en el repositorio local.", "level": "Junior"},
    {"prompt": "2. What does 'deprecated' mean in software development?", "options": ["A) Critical for security.", "B) Recommended for new projects.", "C) Being phased out and shouldn't be used.", "D) Runs faster than normal."], "correct": "C", "explanation": "'Deprecated' indica que algo está obsoleto.", "level": "Junior"},
    {"prompt": "3. [Passive Voice] 'The bug _____ yesterday by the QA team.'", "options": ["A) was found", "B) is finding", "C) found", "D) has find"], "correct": "A", "explanation": "Voz pasiva en pasado simple ('was found').", "level": "Junior"},
    {"prompt": "4. [Interview] How do you politely explain your current role?", "options": ["A) I am responsible for maintaining the frontend code.", "B) I am make the HTML pages.", "C) My job is do CSS style.", "D) I have responsibility to writing code."], "correct": "A", "explanation": "'I am responsible for + [verbo -ing]' es la forma correcta.", "level": "Junior"},
    {"prompt": "5. What is 'responsive design'?", "options": ["A) Website that answers emails.", "B) Design that adapts smoothly to different screen sizes.", "C) Website built only for desktop.", "D) Backend query style."], "correct": "B", "explanation": "Adapta la interfaz a distintas pantallas.", "level": "Junior"},
    {"prompt": "6. CSS: 'The button is hidden because its property is set to _____.'", "options": ["A) display: none", "B) view: false", "C) hide: true", "D) show: off"], "correct": "A", "explanation": "'display: none' oculta el elemento.", "level": "Junior"},
    {"prompt": "7. Standup: 'Yesterday I _____ on fixing the authentication module.'", "options": ["A) work", "B) was worked", "C) worked", "D) have work"], "correct": "C", "explanation": "Pasado simple ('worked').", "level": "Junior"},
    {"prompt": "8. What does 'pull request' (PR) mean?", "options": ["A) Request to download a file.", "B) Proposal to merge code changes into a main repo.", "C) Server error message.", "D) Database query."], "correct": "B", "explanation": "Propuesta para integrar cambios de código.", "level": "Junior"},
    {"prompt": "9. [Interview] 'What tools do you use for version control?'", "options": ["A) I am using Git every day for manage code.", "B) I mainly use Git and GitHub to manage my codebase.", "C) I use Git for make save files.", "D) I have used Git for store my pictures."], "correct": "B", "explanation": "Respuesta profesional y bien estructurada.", "level": "Junior"},
    {"prompt": "10. 'The application is running _____ port 8080.'", "options": ["A) in", "B) at", "C) on", "D) under"], "correct": "C", "explanation": "Se usa 'on' para puertos ('on port 8080').", "level": "Junior"},
    {"prompt": "11. What is the meaning of 'to roll back'?", "options": ["A) Deploy code to production.", "B) Revert software to a previous stable version.", "C) Scroll down rapidly.", "D) Encrypt passwords."], "correct": "B", "explanation": "'Roll back' es restaurar a una versión previa.", "level": "Mid"},
    {"prompt": "12. [Passive Voice] 'All sensitive user data _____ before being stored.'", "options": ["A) must encrypt", "B) must be encrypted", "C) must encrypts", "D) must being encrypted"], "correct": "B", "explanation": "Voz pasiva con modal ('must be + participio').", "level": "Mid"},
    {"prompt": "13. [Interview] How do you explain a past failure?", "options": ["A) It was completely the client's fault.", "B) We hit a roadblock, but I learned how to handle edge cases better.", "C) I don't remember any mistake.", "D) My team broke the code."], "correct": "B", "explanation": "'Hit a roadblock' y mostrar aprendizaje es clave.", "level": "Mid"},
    {"prompt": "14. What does 'refactoring' code mean?", "options": ["A) Rewrite in another language.", "B) Restructuring existing code without changing external behavior.", "C) Fixing syntax errors.", "D) Adding new features."], "correct": "B", "explanation": "Mejora la estructura interna sin cambiar comportamiento.", "level": "Mid"},
    {"prompt": "15. 'If we _____ the database query, response time will decrease.'", "options": ["A) optimize", "B) optimized", "C) will optimize", "D) optimizing"], "correct": "A", "explanation": "Primer condicional (If + presente simple).", "level": "Mid"},
    {"prompt": "16. 'We spent hours trying to figure out the bug.' 'Figure out' means:", "options": ["A) Delete", "B) Discover or solve", "C) Report", "D) Ignore"], "correct": "B", "explanation": "'Figure out' es descubrir o resolver.", "level": "Mid"},
    {"prompt": "17. 'Please make sure to catch potential exceptions.' 'Catch' means:", "options": ["A) Hold the server.", "B) Handle errors gracefully during execution.", "C) Create a variable.", "D) Suppress errors."], "correct": "B", "explanation": "Manejo de errores con try/catch.", "level": "Mid"},
    {"prompt": "18. [Passive Voice] 'The new feature _____ by the staging server right now.'", "options": ["A) is being processed", "B) is processing", "C) was process", "D) has processed"], "correct": "A", "explanation": "Presente continuo pasivo ('is being + participio').", "level": "Mid"},
    {"prompt": "19. [Interview] How to discuss salary expectations?", "options": ["A) I want a lot of money.", "B) Based on my experience and research, I am looking for a range between $X and $Y.", "C) Give me maximum salary.", "D) I don't care about salary."], "correct": "B", "explanation": "Forma profesional con rango estimado.", "level": "Mid"},
    {"prompt": "20. HTTP 404 status code means:", "options": ["A) Found", "B) Not found", "C) Created", "D) Forbidden"], "correct": "B", "explanation": "HTTP 404 = Not Found.", "level": "Mid"},
    {"prompt": "21. [Passive Voice] 'Had the security patch _____ in time, the breach could have been prevented.'", "options": ["A) deployed", "B) been deployed", "C) being deployed", "D) be deploy"], "correct": "B", "explanation": "Inversión condicional pasada pasiva.", "level": "Senior"},
    {"prompt": "22. What does 'out of the box' imply?", "options": ["A) Requires complex setup.", "B) Functionality that works immediately without extra configuration.", "C) Memory overflow error.", "D) Highly experimental."], "correct": "B", "explanation": "Funciona listo para usar sin configuración.", "level": "Senior"},
    {"prompt": "23. [Interview] Senior question about tech stack choices:", "options": ["A) Why React? Vue is better.", "B) Could you walk me through the trade-offs you considered when choosing React?", "C) Why React instead of superior tools?", "D) Who decided this?"], "correct": "B", "explanation": "Evalúa criterios técnicos y trade-offs.", "level": "Senior"},
    {"prompt": "24. What does 'scope creep' refer to in Scrum?", "options": ["A) Uncontrolled growth in project requirements.", "B) Developer pushing to main.", "C) Moving tasks to sprint.", "D) Speed of paying technical debt."], "correct": "A", "explanation": "Crecimiento no planificado del proyecto.", "level": "Senior"},
    {"prompt": "25. Post-mortem incident report (mixed conditional):", "options": ["A) If we had refactored the legacy code last month, our app would be much faster today.", "B) If we refactor, it would be fast.", "C) If we would have refactored, app will be faster.", "D) If we refactored, app was faster."], "correct": "A", "explanation": "Condicional mixto (Causa pasada -> Efecto presente).", "level": "Senior"},
    {"prompt": "26. 'We need to _____ and drop non-essential features.'", "options": ["A) hit the sack", "B) bite the bullet", "C) touch base", "D) reinvent the wheel"], "correct": "B", "explanation": "'Bite the bullet' = tomar una decisión difícil.", "level": "Senior"},
    {"prompt": "27. What does 'technical debt' refer to?", "options": ["A) Money owed to hosting providers.", "B) Implied cost of additional rework caused by choosing an easy solution now.", "C) Salary paid to juniors.", "D) Software licenses."], "correct": "B", "explanation": "Costo diferido por tomar atajos en código.", "level": "Senior"},
    {"prompt": "28. [Interview] Handling system design disagreement:", "options": ["A) Insist my approach is standard.", "B) Acknowledge alternative patterns and defend choice using metrics.", "C) Change opinion immediately.", "D) Refuse to discuss."], "correct": "B", "explanation": "Defender decisiones con métricas y datos.", "level": "Senior"},
    {"prompt": "29. What does 'decoupling' mean?", "options": ["A) Disconnect power.", "B) Separating components so changes in one don't force changes in another.", "C) Merge backend and frontend.", "D) Delete dependencies."], "correct": "B", "explanation": "Desacoplar componentes independientes.", "level": "Senior"},
    {"prompt": "30. [Passive Voice] 'Had microservices not been adopted, the platform _____ scalable enough.'", "options": ["A) won't be", "B) wouldn't have been", "C) isn't being", "D) had not been"], "correct": "B", "explanation": "Tercer condicional en voz pasiva.", "level": "Senior"}
]

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
            st.session_state.started = True
            st.rerun()
        else:
            st.warning("Ingresa un nombre antes de comenzar.")

elif st.session_state.started and not st.session_state.finished:
    q_index = st.session_state.current_q
    question = QUESTIONS[q_index]
    total_q = len(QUESTIONS)

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
    total_q = len(QUESTIONS)
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