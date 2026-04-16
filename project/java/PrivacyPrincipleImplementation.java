package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  Documentation of how a specific privacy principle from Clause 6 has been implemented within the organization's privacy framework, including measures taken and evidence of adherence.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PrivacyPrincipleImplementation extends NamedEntity {

  private String principle;
  private List<String> implementationMeasures;
  private List<PrivacyControl> applicableControlsRef;
  private List<String> evidenceOfAdherence;
  private List<String> gapsIdentified;
  private List<String> improvementActions;
  private LocalDate lastAssessedDate;

}