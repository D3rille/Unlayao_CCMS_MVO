from django.shortcuts import render
from django.http import HttpResponse

def mission(request):
    return HttpResponse(
        """
        <h1>College of Computing and Multimedia Studies</h1>
        <hr/>
        <h2>MISSION</h2>
        <p>The College of Computing and Multimedia Studies shall produce competent and innovative 
        professionals or Technopreneurs in the Information and Communication Technology (ICT) industry 
        adequately prepared in the practice of their profession supportive of national development goals 
        and standards of global excellence.</p>
        """
    )
def vision(request):
    return HttpResponse(
        
        """
        <h1>College of Computing and Multimedia Studies</h1>
        <hr/>
        <h2>VISION</h2>
        <p>The College of Computing and Multimedia Studies shall be a center of excellence in delivering 
        Computing and Multimedia education.</p>
        """
    )
def objectives(request):
    return HttpResponse(
        """
        <h1>College of Computing and Multimedia Studies</h1>
        <hr/>
        <h2>CCMS PROGRAM EDUCATIONAL OBJECTIVES</h2>
        <p>After graduation, alumni of MSEUF-CCMS programs shall:</p>
        <ol>
            <li>Be employed and demonstrate professionalism, competence, and passion
            in solving contemporary computing problems by developing or utilizing innovative IT solutions.</li>
            <li>Embark in lifelong learning or research to attune to the continuous innovation in the IT
            industry in order to adapt to the changing demands of the global market; and</li>
            <li>Exhibit leadership and teamwork, and commitment to their respective local or global organizations.</li>
        </ol>
        """
    )