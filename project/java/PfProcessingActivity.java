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
  Something the organization does with PII: why, on what basis, what it does to which PII, who is responsible, and how long the PII is kept.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PfProcessingActivity  {

  private List<String> pfPurposes;
  private List<String> pfLegalBases;
  private List<String> pfOperations;
  private List<PfPiiItem> pfConcernedPii;
  private String pfRetention;
  private List<PfControl> pfRelatedControls;
  private PfPiiController pfController;
  private List<PfPiiProcessor> pfProcessors;
  private List<PfPiiFlow> pfActivityFlows;
  private List<String> pfSensitivities;
  private Boolean pfCrossesBorders;
  private List<String> pfTransferSafeguards;
  private URI pfId;
  private String title;
  private String description;


}