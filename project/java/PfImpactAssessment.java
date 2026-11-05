package example;

/* metamodel_version: 1.12.0 */
/* version: 2024 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A review of what a system or activity could do to people's privacy, the risks it found and what became of them.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PfImpactAssessment  {

  private String pfAssessmentScope;
  private LocalDate pfAssessmentDate;
  private String pfAssessor;
  private List<PfProcessingActivity> pfAssessedActivities;
  private List<PfRisk> pfRisksFound;
  private List<PfRisk> pfRisksTreated;
  private List<PfRisk> pfRisksAccepted;
  private String pfAssessmentOutcome;
  private List<String> pfConsultations;
  private LocalDate pfNextAssessment;
  private URI pfId;
  private String title;
  private String description;


}